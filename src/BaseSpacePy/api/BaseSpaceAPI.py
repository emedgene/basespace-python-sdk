"""
Copyright 2012 Illumina

    Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pprint import pprint
import urllib2
import shutil
import urllib
import pycurl
import httplib
import cStringIO
import json
import os
import re
from tempfile import mkdtemp
import socket
#import requests

from BaseSpacePy.api.APIClient import APIClient
from BaseSpacePy.api.BaseAPI import BaseAPI
from BaseSpacePy.api.BaseSpaceException import * #@UnusedWildImport
from BaseSpacePy.model.MultipartDownload import MultipartUpload as mpu #@UnresolvedImport
from BaseSpacePy.model.MultipartDownload import MultipartDownload as mpd #@UnresolvedImport
from BaseSpacePy.model.QueryParameters import QueryParameters as qp #@UnresolvedImport
from BaseSpacePy.model import * #@UnusedWildImport

# Uris for obtaining a access token, user verification code, and app trigger information
tokenURL                   = '/oauthv2/token'
deviceURL                  = "/oauthv2/deviceauthorization"
webAuthorize               = '/oauth/authorize'


class BaseSpaceAPI(BaseAPI):
    '''
    The main API class used for all communication with the REST server
    '''
    def __init__(self, clientKey, clientSecret, apiServer, version, appSessionId='', AccessToken='', timeout=10):
        if not apiServer[-1]=='/': apiServer = apiServer + '/'
        #if not version[-1]=='/': version = version + '/'
        
        self.appSessionId   = appSessionId
        self.key            = clientKey
        self.secret         = clientSecret
        self.apiServer      = apiServer + version
        self.version        = version
        self.weburl         = apiServer.replace('api.','')        
        super(BaseSpaceAPI, self).__init__(AccessToken, timeout)


    def __getTriggerObject__(self,obj):
        '''
        Warning this method is not for general use and should only be called 
        from the getAppSession.
        :param obj: The appTrigger json 
        '''
        response = obj
        if response['ResponseStatus'].has_key('ErrorCode'):
            raise Exception('BaseSpace error: ' + str(response['ResponseStatus']['ErrorCode']) + ": " + response['ResponseStatus']['Message'])
        tempApi   = APIClient(AccessToken='', apiServer=self.apiServer)
        response  = tempApi.deserialize(obj, AppSessionResponse.AppSessionResponse) #@UndefinedVariable
        res = response.Response
        res = res.__serializeReferences__(self)
        return res
    
    def __serializeObject__(self,d,type):
        tempApi   = APIClient(AccessToken='', apiServer=self.apiServer)
        if type.lower()=='project':
            return tempApi.deserialize(d, Project.Project)
        if type.lower()=='sample':
            return tempApi.deserialize(d, Sample.Sample)
        if type.lower()=='appresult':
            return tempApi.deserialize(d, AppResult.AppResult)        
        return d
        
    

    def getAppSessionById(self,id):
        '''
        Returns the appSession identified by id
        
        :param id: The id of the appSession
        '''
        # TO_DO make special case for access-token only retrieval
        
        return self.getAppSession(Id=id)

    def getAppSession(self,Id=''):
        '''
        Returns an AppSession instance containing user and data-type the app was triggered by/on 
        :param Id: (Optional) The AppSessionId, id not supplied the AppSessionId used for instantiating
        the BaseSpaceAPI instance.
        
        :param Id: (Optional) AppSession id, if not supplied the AppSession id used to initialize the 
        '''
        
        if (not self.appSessionId) and (not Id):
            raise Exception("This BaseSpaceAPI instance has no appSessionId set and no alternative id was supplied for method getAppSession")
        if (not id) and (not self.key):
            raise Exception("This BaseSpaceAPI instance has no client_secret (key) set and no alternative id was supplied for method getAppSession")
        
        resourcePath = self.apiServer + '/appsessions/{AppSessionId}'
        if not Id:
            resourcePath = resourcePath.replace('{AppSessionId}', self.appSessionId)
        else:
            resourcePath = resourcePath.replace('{AppSessionId}', Id)
        #print resourcePath
        response = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL,resourcePath)
        c.setopt(pycurl.USERPWD,self.key + ":" + self.secret)
        c.setopt(c.WRITEFUNCTION, response.write)
        c.perform()
        c.close()
        obj = json.loads(response.getvalue())
        # TODO add exception if response isn't OK, e.g. incorrect server gives path not recognized
        return self.__getTriggerObject__(obj) 


    def getAppSessionPropertiesById(self, Id, queryPars=None):
        '''
        Returns the Properties of an AppSession
        :param Id: The AppSessionId            
        '''                
        if queryPars is None:
            queryPars = qp()
        resourcePath = '/appsessions/{Id}/properties'
        resourcePath = resourcePath.replace('{Id}',Id)
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}                
        return self.__singleRequest__(PropertiesResponse.PropertiesResponse, resourcePath, method, queryParams, headerParams, verbose=0)


    def getAppSessionPropertyByName(self, Id, queryPars=None, name=''):
        '''
        Returns the multi-value Property of the provided AppSession that has the provided Property name.
        Note - this method (and REST API) is supported for ONLY multi-value Properties.
        :param Id: The AppSessionId
        :param name: Name of the multi-value property to retrieve        
        '''                
        if queryPars is None:
            queryPars = qp()        
        resourcePath = '/appsessions/{Id}/properties/{Name}/items'
        resourcePath = resourcePath.replace('{Id}', Id)
        resourcePath = resourcePath.replace('{Name}', name)        
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(MultiValuePropertyResponse.MultiValuePropertyResponse, resourcePath, method, queryParams, headerParams, verbose=0)
                    

    def getAppSessionInputsById(self, Id, queryPars=None):
        '''
        Returns a dictionary of input properties from the provided AppSessions, keyed by input Name        
        '''
        if queryPars is None:
            queryPars = qp()        
        props = self.getAppSessionPropertiesById(Id, queryPars)
        inputs = {}
        for prop in props.Items:
            match = re.search("^Input\.(.+)", prop.Name)
            if match != None:
                inputs[match.group(1)] = prop
        return inputs
                
    def getAccess(self,obj,accessType='write',web=0,redirectURL='',state=''):
        '''
        
        :param obj: The data object we wish to get access to
        :param accessType: (Optional) the type of access (read|write), default is write
        :param web: (Optional) true if the App is web-based, default is false meaning a device based app
        :param redirectURL: (Optional) For the web-based case, a
        :param state: (Optional)
        '''
        scopeStr = obj.getAccessStr(scope=accessType)
        if web:
            return self.getWebVerificationCode(scopeStr, redirectURL, state)
        else:
            return self.getVerificationCode(scopeStr)
        
    def getVerificationCode(self,scope,):
        '''
        Returns the BaseSpace dictionary containing the verification code and verification url for the user to approve
        access to a specific data scope.  
        
        Corresponding curl call:
        curlCall = 'curl -d "response_type=device_code" -d "client_id=' + client_key + '" -d "scope=' + scope + '" ' + deviceURL
        
        For details see:
        https://developer.basespace.illumina.com/docs/content/documentation/authentication/obtaining-access-tokens
            
        :param scope: The scope that access is requested for
        '''
#        curlCall = 'curl -d "response_type=device_code" -d "client_id=' + self.key + '" -d "scope=' + scope + '" ' + self.apiServer + deviceURL
#        print curlCall
        if (not self.key):
            raise Exception("This BaseSpaceAPI instance has no client_secret (key) set and no alternative id was supplied for method getVerificationCode")
        data = [('client_id',self.key),('scope', scope),('response_type','device_code')]
        return self.__makeCurlRequest__(data,self.apiServer + deviceURL)

    def getWebVerificationCode(self,scope,redirectURL,state=''):
        '''
        Generates the URL the user should be redirected to for web-based authentication
         
        :param scope: The scope that access is requested for
        :param redirectURL: The redirect URL
        :state: An optional state parameter that will passed through to the redirect response
        '''
        
        if (not self.key):
            raise Exception("This BaseSpaceAPI instance has no client_id (key) set and no alternative id was supplied for method getVerificationCode")
        data = {'client_id':self.key,'redirect_uri':redirectURL,'scope':scope,'response_type':'code',"state":state}
        return self.weburl + webAuthorize + '?' + urllib.urlencode(data)

    def obtainAccessToken(self,code,grantType='device',redirect_uri='http://www.myRedirect.com'):
        '''
        Returns a user specific access token.    
        
        :param code: The device code returned by the verification code method
        :param grantType: Grant-type may be either device or 'device' or 'authorization_code' 
        :param redirect_uri: The uri we should redirect to
        '''
        if (not self.key) or (not self.secret):
            raise Exception("This BaseSpaceAPI instance has either no client_secret or no client_id set and no alternative id was supplied for method getVerificationCode")
        data = [('client_id',self.key),('client_secret', self.secret),('code',code),('grant_type',grantType),('redirect_uri',redirect_uri)]
        dict = self.__makeCurlRequest__(data,self.apiServer + tokenURL)
        return dict['access_token']

    def updatePrivileges(self,code,grantType='device',redirect_uri='http://www.myRedirect.com'):
        token = self.obtainAccessToken(code,grantType=grantType,redirect_uri=redirect_uri)
        self.setAccessToken(token)
            
    def createProject(self,Name):
        '''
        Creates a project with the specified name and returns a project object. 
        If a project with this name already exists, the existing project is returned.
        
        :param Name: Name of the project
        '''        
        #: v1pre3/projects, it requires 1 input parameter which is Name
        resourcePath            = '/projects/'
        resourcePath            = resourcePath.replace('{format}', 'json')
        method                  = 'POST'
        queryParams             = {}
        headerParams            = {}
        postData                = {}
        postData['Name']        = Name
        
        return self.__singleRequest__(ProjectResponse.ProjectResponse,resourcePath, method, queryParams, headerParams,postData=postData,verbose=0)
            
    
    def getUserById(self, Id, ):
        '''
        Returns the User object corresponding to Id
        
        :param Id: The Id of the user
        '''
        # Parse inputs
        resourcePath = '/users/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryParams = {}
        headerParams = {}
        return self.__singleRequest__(UserResponse.UserResponse,resourcePath, method, queryParams, headerParams)
           
    def getAppResultById(self, Id, queryPars=None):
        '''
        Returns an AppResult object corresponding to Id
        
        :param Id: The Id of the AppResult
        '''
        # Parse inputs
        if queryPars is None:
            queryPars = qp()        
        resourcePath = '/appresults/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(AppResultResponse.AppResultResponse,resourcePath, method, queryParams, headerParams)

    def getAppResultPropertiesById(self, Id, queryPars=None):
        '''
        Returns the Properties of an AppResult object corresponding to Id
        
        :param Id: The Id of the AppResult
        '''
        # Parse inputs
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/appresults/{Id}/properties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(PropertiesResponse.PropertiesResponse, resourcePath, method, queryParams, headerParams)

    def getAppResultFiles(self, Id, queryPars=None):
        '''
        Returns a list of File object for the AppResult with id  = Id
        
        :param Id: The id of the appresult.
        :param queryPars: An (optional) object of type QueryParameters for custom sorting and filtering 
        '''
        # Parse inputs
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/appresults/{Id}/files'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}',Id)
        return self.__listRequest__(File.File,resourcePath, method, queryParams, headerParams,verbose=0)

    def getProjectById(self, Id, queryPars=None):
        '''
        Request a project object by Id
        
        :param Id: The Id of the project
        '''
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/projects/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(ProjectResponse.ProjectResponse,resourcePath, method, queryParams, headerParams)

    def getProjectPropertiesById(self, Id, queryPars=None):
        '''
        Request the Properties of a project object by Id
        
        :param Id: The Id of the project
        '''
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/projects/{Id}/properties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(PropertiesResponse.PropertiesResponse,resourcePath, method, queryParams, headerParams)
           
    def getProjectByUser(self, Id, queryPars=None):
        '''
        Returns a list available projects for a User with the specified Id
        
        :param Id: The id of the user
        :param qp: An (optional) object of type QueryParameters for custom sorting and filtering
        '''
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/users/{Id}/projects'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        if Id != None: resourcePath = resourcePath.replace('{Id}', Id)
        return self.__listRequest__(Project.Project,resourcePath, method, queryParams, headerParams)
       
    def getAccessibleRunsByUser(self, Id, queryPars=None):
        '''
        Returns a list of accessible runs for the User with id=Id
        
        :param Id: An user id
        :param queryPars: An (optional) object of type QueryParameters for custom sorting and filtering
        '''        
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/users/{Id}/runs'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}',Id)
        return self.__listRequest__(RunCompact.RunCompact,resourcePath, method, queryParams, headerParams)
    
    def getRunById(self, Id, queryPars=None):
        '''        
        Request a run object by Id
        
        :param Id: The Id of the run
        '''        
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/runs/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()        
        headerParams = {}
        return self.__singleRequest__(RunResponse.RunResponse,resourcePath, method, queryParams, headerParams)
    
    def getRunPropertiesById(self, Id, queryPars=None):
        '''        
        Request the Properties of a run object by Id
        
        :param Id: The Id of the run
        '''        
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/runs/{Id}/properties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(PropertiesResponse.PropertiesResponse,resourcePath, method, queryParams, headerParams)
    
    def getAppResultsByProject(self, Id, queryPars=None, statuses=None):
        '''
        Returns a list of AppResult object associated with the project with Id
        
        :param Id: The project id
        :param queryPars: An (optional) object of type QueryParameters for custom sorting and filtering
        :param statuses: An (optional) list of AppResult statuses to filter by
        '''
        if queryPars is None:
            queryPars = qp() 
        if statuses is None:
            statuses = []               
        resourcePath = '/projects/{Id}/appresults'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        if len(statuses): queryParams['Statuses'] = ",".join(statuses)
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}',Id)
        return self.__listRequest__(AppResult.AppResult,resourcePath, method, queryParams, headerParams,verbose=0)

    def getSamplesByProject(self, Id, queryPars=None):
        '''
        Returns a list of samples associated with a project with Id
        
        :param Id: The id of the project
        :param queryPars: An (optional) object of type QueryParameters for custom sorting and filtering
        '''
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/projects/{Id}/samples'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}',Id)
        return self.__listRequest__(Sample.Sample,resourcePath, method, queryParams, headerParams,verbose=0)

    def getSampleById(self, Id, queryPars=None):
        '''
        Returns a Sample object
        
        :param Id: The id of the sample
        '''
        if queryPars is None:
            queryPars = qp()        
        resourcePath = '/samples/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(SampleResponse.SampleResponse,resourcePath, method, queryParams, headerParams, verbose=0)
    
    def getSamplePropertiesById(self, Id, queryPars=None):
        '''
        Returns the Properties of a Sample object
        
        :param Id: The id of the sample
        '''
        if queryPars is None:
            queryPars = qp()                        
        resourcePath = '/samples/{Id}/properties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__singleRequest__(PropertiesResponse.PropertiesResponse, resourcePath, method, queryParams, headerParams, verbose=0)    

    def getFilesBySample(self, Id, queryPars=None):
        '''
        Returns a list of File objects associated with sample with Id
        
        :param Id: A Sample id
        :param queryPars: An (optional) object of type QueryParameters for custom sorting and filtering
        '''
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/samples/{Id}/files'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}',Id)
        return self.__listRequest__(File.File,resourcePath, method, queryParams, headerParams,verbose=0)
    
    def getFileById(self, Id, queryPars=None):
        '''
        Returns a file object by Id
        
        :param Id: The id of the file
        '''
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/files/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()        
        headerParams = {}
        return self.__singleRequest__(FileResponse.FileResponse,resourcePath, method,\
                                      queryParams, headerParams,verbose=0)
        
    def getFilePropertiesById(self, Id, queryPars=None):
        '''
        Returns the Properties of a file object by Id
        
        :param Id: The id of the file
        '''        
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/files/{Id}/properties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryPars.validate()
        queryParams = queryPars.getParameterDict()        
        headerParams = {}
        return self.__singleRequest__(PropertiesResponse.PropertiesResponse, resourcePath, method,\
                                      queryParams, headerParams,verbose=0)

    def getGenomeById(self, Id, ):
        '''
        Returns an instance of Genome with the specified Id
        
        :param Id: The genome id
        '''
        # Parse inputs
        resourcePath = '/genomes/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryParams = {}
        headerParams = {}
        return self.__singleRequest__(GenomeResponse.GenomeResponse,resourcePath, method, queryParams, headerParams)

    def getAvailableGenomes(self, queryPars=None):
        '''
        Returns a list of all available genomes
        
        :param queryPars: An (optional) object of type QueryParameters for custom sorting and filtering
        '''        
        if queryPars is None:
            queryPars = qp()                
        resourcePath = '/genomes'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        return self.__listRequest__(GenomeV1.GenomeV1,resourcePath, method, queryParams, headerParams,verbose=0)
    
    # TODO, needs more work in parsing meta data, currently only map keys are returned 
    
    def getVariantMetadata(self, Id, Format,):
        '''
        Returns a VariantMetadata object for the variant file
        
        :param Id: The Id of the VCF file
        :param Format: Set to 'vcf' to get the results as lines in VCF format
        '''
        # Parse inputs
        resourcePath = '/variantset/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryParams = {}
        headerParams = {}
        queryParams['Format'] = self.apiClient.toPathValue(Format)
        resourcePath = resourcePath.replace('{Id}', Id)
        return self.__singleRequest__(VariantsHeaderResponse.VariantsHeaderResponse,resourcePath, method,\
                                      queryParams, headerParams,verbose=0)
    
    def filterVariantSet(self,Id, Chrom, StartPos, EndPos, Format, queryPars=None):
        '''
        List the variants in a set of variants. Maximum returned records is 1000
        
        :param Id: The id of the variant file 
        :param Chrom: The chromosome of interest
        :param StartPos: The start position of the sequence of interest
        :param EndPos: The start position of the sequence of interest
        :param Format: Set to 'vcf' to get the results as lines in VCF format (default is 'json')
        :param queryPars: An (optional) object of type QueryParameters for custom sorting and filtering
        '''
        if queryPars is None:
            queryPars=qp(pars={'SortBy':'Position'})
        resourcePath = '/variantset/{Id}/variants/{Chrom}'
        method = 'GET'
        queryPars.validate()
        queryParams = queryPars.getParameterDict()
        headerParams = {}
        queryParams['StartPos'] = StartPos
        queryParams['EndPos']   = EndPos
        queryParams['Format']   = Format
        resourcePath = resourcePath.replace('{Chrom}', Chrom)
        resourcePath = resourcePath.replace('{Id}', Id)
        return self.__listRequest__(Variant.Variant,resourcePath, method, queryParams, headerParams,verbose=0)
    
    def getIntervalCoverage(self, Id, Chrom, StartPos=None, EndPos=None, ):
        '''
        Mean coverage levels over a sequence interval
        
        :param Id: Chromosome to query
        :param Chrom: The Id of the resource
        :param StartPos: Get coverage starting at this position. Default is 1
        :param EndPos: Get coverage up to and including this position. Default is StartPos + 1280
        
        :return:CoverageResponse -- an instance of CoverageResponse
        '''
        # Parse inputs
        resourcePath = '/coverage/{Id}/{Chrom}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryParams = {}
        headerParams = {}
        queryParams['StartPos'] = self.apiClient.toPathValue(StartPos)
        queryParams['EndPos'] = self.apiClient.toPathValue(EndPos)
        resourcePath = resourcePath.replace('{Chrom}', Chrom)
        resourcePath = resourcePath.replace('{Id}', Id)
        return self.__singleRequest__(CoverageResponse.CoverageResponse,resourcePath, method,\
                                      queryParams, headerParams,verbose=0)

    def getCoverageMetaInfo(self, Id, Chrom):
        '''
        Returns Metadata about coverage as a CoverageMetadata instance
        
        :param Id: he Id of the Bam file 
        :param Chrom: Chromosome to query
        '''
        # Parse inputs
        resourcePath = '/coverage/{Id}/{Chrom}/meta'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryParams = {}
        headerParams = {}
        resourcePath = resourcePath.replace('{Chrom}', Chrom)
        resourcePath = resourcePath.replace('{Id}', Id)
        
        return self.__singleRequest__(CoverageMetaResponse.CoverageMetaResponse,resourcePath, method,\
                                      queryParams, headerParams,verbose=0)
     
    def createAppResult(self, Id, name, desc, samples=None, appSessionId=None):
        '''
        Create an AppResult object
        
        :param Id: The id of the project in which the AppResult is to be added
        :param name: The name of the AppResult
        :param desc: A describtion of the AppResult
        :param samples: (Optional) The samples 
        :param appSessionId: (Optional) If no appSessionId is given, the id used to initialize the BaseSpaceAPI instance
        will be used. If appSessionId is set equal to an empty string, a new appsession will be created for the appresult object 
        '''
        if (not self.appSessionId) and (appSessionId==None):
            raise Exception("This BaseSpaceAPI instance has no appSessionId set and no alternative id was supplied for method createAppResult")
        if samples is None:
            samples = []
        resourcePath = '/projects/{ProjectId}/appresults'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'
        resourcePath = resourcePath.replace('{ProjectId}', Id)
        queryParams = {}
        headerParams = {}
        postData = {}
        
        if appSessionId:        queryParams['appsessionid'] = appSessionId
        if appSessionId==None:  queryParams['appsessionid'] = self.appSessionId      # default case, we use the current appsession
        
        # add the sample references
        if len(samples):
            ref = []
            for s in samples:
                d = {"Rel":"using","Type": "Sample", "HrefContent": self.version + '/samples/' + s.Id}
                ref.append(d)
            postData['References']  = ref
        # case, an appSession is provided, we need to check if the a
        if queryParams.has_key('appsessionid'):
            session = self.getAppSession(Id=queryParams['appsessionid'])
            if not session.canWorkOn():
                raise Exception('AppSession status must be "running," to create and AppResults. Current status is ' + session.Status)
            
        postData['Name']        = name
        postData['Description'] = desc
        return self.__singleRequest__(AppResultResponse.AppResultResponse,resourcePath, method, queryParams, headerParams,postData=postData,verbose=0)
            
    def appResultFileUpload(self, Id, localPath, fileName, directory, contentType, multipart=0):
        '''
        Uploads a file associated with an AppResult to BaseSpace and returns the corresponding file object  
        
        :param Id: AppResult id.
        :param localPath: The local path to the file to be uploaded.
        :param fileName: The desired filename in the AppResult folder on the BaseSpace server.
        :param directory: The directory the file should be placed in.
        :param contentType: The content-type of the file.
         
        '''
        resourcePath = '/appresults/{Id}/files'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'
        resourcePath                 = resourcePath.replace('{Id}', Id)
        queryParams                  = {}
        queryParams['name']          = fileName
        queryParams['directory']     = directory 
        headerParams                 = {}
        headerParams['Content-Type'] = contentType
        
        # three cases, two for multipart, starting 
        if multipart==1:
            queryParams['multipart']          = 'true'
            postData = None
            # Set force post as this need to use POST though no data is being streamed
            return self.__singleRequest__(FileResponse.FileResponse,resourcePath, method,\
                                      queryParams, headerParams,postData=postData,verbose=0,forcePost=1)
        else:
            postData                     = open(localPath).read()
            return self.__singleRequest__(FileResponse.FileResponse,resourcePath, method,\
                                      queryParams, headerParams,postData=postData,verbose=0)

    def fileDownload(self, Id, localDir, byteRange=None):
        '''
        Downloads a BaseSpace file to a local directory, and names the file with the BaseSpace file name.
        If the file is large, use multi-part download.
        Byte-range requests are supported for only small byte ranges (single-part downloads).
        Returns file object when complete, exception raised if download fails.
        
        Byte-range requests are restricted to a single request of 'start' and 'end' bytes, without support for
        negative or empty values for 'start' or 'end'.
        
        :param Id: The file id
        :param localDir: The local directory to place the file in    
        :param byteRange: (optional) The byte range of the file to retrieve, provide a 2-element list with start and end byte values        
        '''
        multipart_min_file_size = 5000000 # bytes
        if byteRange:
            try:
                rangeSize = byteRange[1] - byteRange[0] + 1
            except IndexError:
                raise ByteRangeException("Byte range must include both start and end byte values")
            if rangeSize <= 0:
                raise ByteRangeException("Byte range must have smaller byte number first")
            if rangeSize > multipart_min_file_size:
                raise ByteRangeException("Byte range %d larger than maximum allowed size %d" % (rangeSize, multipart_min_file_size))
        
        bs_file = self.getFileById(Id)
        if (bs_file.Size < multipart_min_file_size) or (byteRange and (rangeSize < multipart_min_file_size)):
            self._downloadFile(Id, localDir, bs_file.Name, byteRange, standaloneRangeFile=True)
            return bs_file
        else:                        
            return self.multipartFileDownload(Id, localDir)

    def _downloadFile(self, Id, localDir, name, byteRange=None, standaloneRangeFile=False, lock=None): #@ReservedAssignment
        '''
        Downloads a BaseSpace file to a local directory. Supports byte-range requests; by default
        will seek() into local file for multipart downloads, with option to save range data in standalone file.                
        
        :param Id: The file id
        :param localDir: The local directory to place the file in
        :param name: The name of the local file
        :param byteRange: (Optional) The byte range of the file to retrieve, provide a 2-element list with start and end byte values
        :param standaloneRangeFile: (Optional) if True store byte-range data in standalone file
        :param lock: (Optional) Multiprocessing lock to prevent multiple processes from writing to same output file concurrently - only needed when using multipart download
        '''
        if byteRange is None:
            byteRange = []
        resourcePath = '/files/{Id}/content'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryParams = {}
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}', Id)
        queryParams['redirect'] = 'meta' # we need to add this parameter to get the Amazon link directly 
        
        response = self.apiClient.callAPI(resourcePath, method, queryParams,None, headerParams)
        if response['ResponseStatus'].has_key('ErrorCode'):
            raise Exception('BaseSpace error: ' + str(response['ResponseStatus']['ErrorCode']) + ": " + response['ResponseStatus']['Message'])
        
        # get the Amazon URL, then do the download; for range requests include
        # size to ensure reading until end of data stream. Create local file if
        # it doesn't exist (don't truncate in case other processes from 
        # multipart download also do this)
        req = urllib2.Request(response['Response']['HrefContent'])
        filename = os.path.join(localDir, name)
        if not os.path.exists(filename):
            open(filename, 'a').close()
        iter_size = 16*1024 # python default
        #headers = {}
        if len(byteRange):
            req.add_header('Range', 'bytes=%s-%s' % (byteRange[0], byteRange[1]))
            #headers = {'Range': 'bytes=%s-%s' % (byteRange[0], byteRange[1]) }            
        flo = urllib2.urlopen(req, timeout=self.timeout) # timeout prevents blocking                
        #r = requests.get(response['Response']['HrefContent'], headers=headers)                                                                     
        tot_read = 0
        with open(filename, 'r+b', 0) as fp:
            if len(byteRange) and standaloneRangeFile == False:
                fp.seek(byteRange[0])
            #with lock:
            #    fp.write(r.content)
            #tot_read = len(r.content)
            cur = flo.read(iter_size)                
            while cur:                             
                if lock is not None:
                    with lock:                           
                        fp.write(cur)
                else:
                    fp.write(cur)
                tot_read += len(cur)
                cur = flo.read(iter_size)
        # check that actual downloaded byte size is correct
        if len(byteRange):
            exp_size = byteRange[1] - byteRange[0] + 1
            if tot_read != exp_size:
                raise Exception("Ranged download size is not as expected: " + str(tot_read) + " vs " + str(exp_size))
        # TODO test that size is correct for non-range requests                     

    def fileUrl(self,Id): #@ReservedAssignment
        '''
        ** Deprecated in favor of fileS3metadata() **
        
        Returns URL of file (on S3)
        
        :param Id: The file id
        '''
        resourcePath = '/files/{Id}/content'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryParams = {}
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}', Id)
        queryParams['redirect'] = 'meta' # we need to add this parameter to get the Amazon link directly 
        
        response = self.apiClient.callAPI(resourcePath, method, queryParams,None, headerParams)
        if response['ResponseStatus'].has_key('ErrorCode'):
            raise Exception('BaseSpace error: ' + str(response['ResponseStatus']['ErrorCode']) + ": " + response['ResponseStatus']['Message'])
        
        # return the Amazon URL 
        return response['Response']['HrefContent']

    def fileS3metadata(self, Id):
        '''
        Returns the S3 url and etag (md5 for small files uploaded as a single part) for a BaseSpace file
                
        :param Id: The file id
        '''
        ret = {}
        resourcePath = '/files/{Id}/content'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'
        queryParams = {}
        headerParams = {}
        resourcePath = resourcePath.replace('{Id}', Id)
        queryParams['redirect'] = 'meta' # we need to add this parameter to get the Amazon link directly 
        
        response = self.apiClient.callAPI(resourcePath, method, queryParams,None, headerParams)
        if response['ResponseStatus'].has_key('ErrorCode'):
            raise Exception('BaseSpace error: ' + str(response['ResponseStatus']['ErrorCode']) + ": " + response['ResponseStatus']['Message'])
        
        # record S3 URL
        ret['url'] = response['Response']['HrefContent']
        
        # TODO should use HEAD call here, instead do small GET range request
        # GET S3 url and record etag         
        req = urllib2.Request(response['Response']['HrefContent'])        
        req.add_header('Range', 'bytes=%s-%s' % (0, 1))         
        flo = urllib2.urlopen(req, timeout=self.timeout) # timeout prevents blocking  
        try:        
            etag = flo.headers['etag']
        except KeyError:
            etag = ''
        # strip quotes from etag
        if etag.startswith('"') and etag.endswith('"'):
            etag = etag[1:-1]
        ret['etag'] = etag                                                
        return ret
               
    def __uploadMultipartUnit__(self, Id, partNumber, md5, data):
        '''
        Helper method, do not call
        
        :param Id: file id 
        :param partNumber: the file part to be uploaded
        :param md5: md5 sum of datastream
        :param data: the data-stream to be uploaded
        '''
        resourcePath                 = '/files/{Id}/parts/{partNumber}'
        resourcePath                 = resourcePath.replace('{format}', 'json')
        method                       = 'PUT'
        resourcePath                 = resourcePath.replace('{Id}', Id)
        resourcePath                 = resourcePath.replace('{partNumber}', str(partNumber))
        queryParams                  = {}
        headerParams                 = {'Content-MD5':md5.strip()}
        out = self.apiClient.callAPI(resourcePath, method, queryParams, data, headerParams=headerParams, forcePost=0)
        return out

    def multipartFileUpload(self, Id, localDir, fileName, directory, contentType, tempDir=None, cpuCount=2, partSize=25, verbose=0):
        '''
        Method for multi-threaded file-upload for parallel transfer of very large files (currently only runs on unix systems)
        The call returns 
        
        :param Id: The AppResult ID
        :param localDir: The local path of the file to be uploaded
        :param fileName: The desired filename on the server
        :param directory: The server directory to place the file in (empty string will place it in the root directory)
        :param contentType: The content type of the file
        :param tempdir: (optional) Temp directory to use for temporary file chunks to upload
        :param cpuCount: The number of CPUs to be used
        :param partSize: The size of individual upload parts (must be >5mb and <=25mb)
        :param verbose: Write process output to stdout as upload progresses
        '''
        # TODO add separate argument for path since local path now gets put into BaseSpace file object
        # TODO create convenience method to auto-determine whether to use single of multi-part upload
        # TODO add validation on part size
        # First create file object in BaeSpace
        bsFile = self.appResultFileUpload(Id, localDir, fileName, directory, contentType, multipart=1)
        
        if tempDir is None:
            tempDir = mkdtemp()
        # TODO add verbose mode
        myMpu = mpu(self, localDir, bsFile, cpuCount, partSize, temp_dir=tempDir)                
        return myMpu.upload()                

    def multipartFileDownload(self, Id, localDir, processCount=4, partSize=8000000, debug=False, tempDir=None):
        '''
        Method for multi-threaded file-download for parallel transfer of very large files (currently only runs on unix systems)
        Returns a file object, exception raised on download failure.
        
        :param Id: The ID of the File to download 
        :param localDir: The local path in which to store the downloaded file
        :param processCount: The number of processes to be used
        :param partSize: The size in bytes of individual download parts
        :param debug: (optional) Debug mode uses tempDir to store chunks of downloaded files, then ends by 'cat'ing chunks into large file
        :param tempDir: (optional) Temp directory to use for debug mode; if not provided, 'localDir' will be used
        '''         
        if not tempDir:
            tempDir = localDir
        myMpd = mpd(self, Id, localDir, processCount, partSize, temp_dir=tempDir, debug=debug)
        bsFile = myMpd.download()
        return bsFile        

    # TODO change name to include upload
    def markFileState(self,Id):
        '''
        Marks a multi-part upload file as complete  
        :param Id: file id.
        '''
        resourcePath = '/files/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'
        resourcePath                 = resourcePath.replace('{Id}', Id)
        headerParams                 = {}
        queryParams              = {'uploadstatus':'complete'}
        postData = None
        
        # Set force post as this need to use POST though no data is being streamed
        return self.__singleRequest__(FileResponse.FileResponse,resourcePath, method,\
                                  queryParams, headerParams,postData=postData,verbose=0,forcePost=1)

    def setAppSessionState(self,Id,Status,Summary):
        '''
        Set the status of an AppResult object
        
        :param Id: The id of the AppResult
        :param Status: The status assignment string must
        :param Summary: The summary string
        '''
        # Parse inputs
        resourcePath = '/appsessions/{Id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'
        resourcePath = resourcePath.replace('{Id}', Id)
        queryParams = {}
        headerParams = {}
        postData = {}
        statusAllowed = ['running', 'complete', 'needsattention', 'aborted','error']
        if not Status.lower() in statusAllowed:
            raise Exception("AppResult state must be in " + str(statusAllowed))
        postData['status'] = Status.lower()
        postData['statussummary'] = Summary
        return self.__singleRequest__(AppSessionResponse.AppSessionResponse,resourcePath, method,\
                                      queryParams, headerParams,postData=postData,verbose=0)

