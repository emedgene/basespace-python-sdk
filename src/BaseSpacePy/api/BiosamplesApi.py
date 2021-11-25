"""
    Basespace API

    Basespace REST API

    OpenAPI spec version: 5.0.0
"""

from __future__ import absolute_import

import re  # noqa: F401
import six

from . import APIClient
from BaseSpacePy.api.BaseAPI import BaseAPI


class BiosamplesApi(BaseAPI):
    def __init__(self, access_token=None, api_server_and_version=None):
        if None in [access_token, api_server_and_version]:
            raise ValueError("AccessToken and api-server-and-version must be specified")
        self.api_client = APIClient.APIClient(AccessToken=access_token, apiServerAndVersion=api_server_and_version)
        super(BiosamplesApi, self).__init__(access_token, api_server_and_version)

    def get_v2_biosamples(self, **kwargs):  # noqa: E501
        """Get a list of biosamples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = biosample_api.get_v2_biosamples(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] biosamplename: Only return biosamples with the given BioSampleName(s)
        :param list[str] include: Sub elements to include in the response
        :param list[str] propertynamestartswith:
        :param list[str] status: Only return biosamples with the given Status(es)
        :param list[str] labstatus: Only return biosamples with the given LabStatus(es)
        :param list[str] projectid: Only return biosamples with the specified default projects or datasets in those projects
        :param str sortby: The field(s) used to sort the result set
        :param int offset: The starting offset to read
        :param int limit: The maximum number of items to return
        :param str sortdir: The sort direction for the result set
        :return: V2BiologicalSampleCompactList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v2_biosamples_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_v2_biosamples_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_v2_biosamples_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of biosamples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = biosample_api.get_v2_biosamples_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] biosamplename: Only return biosamples with the given BioSampleName(s)
        :param list[str] include: Sub elements to include in the response
        :param list[str] propertynamestartswith:
        :param list[str] status: Only return biosamples with the given Status(es)
        :param list[str] labstatus: Only return biosamples with the given LabStatus(es)
        :param list[str] projectid: Only return biosamples with the specified default projects or datasets in those projects
        :param str sortby: The field(s) used to sort the result set
        :param int offset: The starting offset to read
        :param int limit: The maximum number of items to return
        :param str sortdir: The sort direction for the result set
        :return: V2BiologicalSampleCompactList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['biosamplename', 'include', 'propertynamestartswith', 'status', 'labstatus', 'projectid',
                      'sortby', 'offset', 'limit', 'sortdir']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v2_biosamples" % key
                )
            params[key] = val
        del params['kwargs']

        query_params = []
        if 'biosamplename' in params:
            query_params.append(('biosamplename', params['biosamplename']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
        if 'propertynamestartswith' in params:
            query_params.append(('propertynamestartswith', params['propertynamestartswith']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'labstatus' in params:
            query_params.append(('labstatus', params['labstatus']))  # noqa: E501
        if 'projectid' in params:
            query_params.append(('projectid', params['projectid']))  # noqa: E501
        if 'sortby' in params:
            query_params.append(('sortby', params['sortby']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sortdir' in params:
            query_params.append(('sortdir', params['sortdir']))  # noqa: E501

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        resource_path = '/biosamples'
        method = 'GET'
        return self.api_client.callAPI(resource_path, method, dict(query_params), None, header_params)
