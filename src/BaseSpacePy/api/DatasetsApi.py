# coding: utf-8

"""
    Basespace API

    Basespace REST API

    OpenAPI spec version: 5.0.0
"""

from __future__ import absolute_import

import re  # noqa: F401
import six

from BaseSpacePy.api.APIClient import APIClient


class DatasetsApi(object):
    def __init__(self, access_token=None, api_server_and_version=None):
        if None in [access_token, api_server_and_version]:
            raise ValueError("AccessToken and api-server-and-version must be specified")
        self.api_client = APIClient(AccessToken=access_token, apiServerAndVersion=api_server_and_version)

    def get_v2_datasets(self, **kwargs):  # noqa: E501
        """Get a list of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_datasets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] include: Can specify to return Properties, which returns an additional properties section for each dataset. Or return AppSessionRoot, which returns information about the root analysis of a workflow in the AppSession section for each dataset it applies to.
        :param list[str] propertyfilters: Specify which properties to include in the properties section, e.g. Input.BioSamples, Input.Libraries, or Input.Runs.
        :param list[str] datasettypes: Return datasets of this type or excluding this type. Supports comma-separated lists.
        :param list[str] qcstatus: Return datasets of this QC status.
        :param list[str] uploadstatus: Return datasets of this file upload status.
        :param list[int] inputbiosamples: Return datasets related to this biosample ID.
        :param list[int] inputruns: Return datasets related to this run ID.
        :param list[str] inputruntokens: Return datasets related to this run ID token.
        :param str projectid: Return datasets related to this project ID.
        :param list[int] appsessionids: Return datasets related to this app session ID.
        :param str isarchived: The archive states to filter by. Valid values include: True, False.
        :param str sortby: The field(s) used to sort the result set
        :param int offset: The starting offset to read
        :param int limit: The maximum number of items to return
        :param str sortdir: The sort direction for the result set
        :return: V2DatasetCompactList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v2_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_v2_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_v2_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] include: Can specify to return Properties, which returns an additional properties section for each dataset. Or return AppSessionRoot, which returns information about the root analysis of a workflow in the AppSession section for each dataset it applies to.
        :param list[str] propertyfilters: Specify which properties to include in the properties section, e.g. Input.BioSamples, Input.Libraries, or Input.Runs.
        :param list[str] datasettypes: Return datasets of this type or excluding this type. Supports comma-separated lists.
        :param list[str] qcstatus: Return datasets of this QC status.
        :param list[str] uploadstatus: Return datasets of this file upload status.
        :param list[int] inputbiosamples: Return datasets related to this biosample ID.
        :param list[int] inputruns: Return datasets related to this run ID.
        :param list[str] inputruntokens: Return datasets related to this run ID token.
        :param str projectid: Return datasets related to this project ID.
        :param list[int] appsessionids: Return datasets related to this app session ID.
        :param str isarchived: The archive states to filter by. Valid values include: True, False.
        :param str sortby: The field(s) used to sort the result set
        :param int offset: The starting offset to read
        :param int limit: The maximum number of items to return
        :param str sortdir: The sort direction for the result set
        :return: V2DatasetCompactList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include', 'propertyfilters', 'datasettypes', 'qcstatus', 'uploadstatus', 'inputbiosamples',
                      'inputruns', 'inputruntokens', 'projectid', 'appsessionids', 'isarchived', 'sortby', 'offset',
                      'limit', 'sortdir']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v2_datasets" % key
                )
            params[key] = val
        del params['kwargs']

        # collection_formats = {}
        # path_params = {}

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            # collection_formats['include'] = 'csv'  # noqa: E501
        if 'propertyfilters' in params:
            query_params.append(('propertyfilters', params['propertyfilters']))  # noqa: E501
            # collection_formats['propertyfilters'] = 'csv'  # noqa: E501
        if 'datasettypes' in params:
            query_params.append(('datasettypes', params['datasettypes']))  # noqa: E501
            # collection_formats['datasettypes'] = 'csv'  # noqa: E501
        if 'qcstatus' in params:
            query_params.append(('qcstatus', params['qcstatus']))  # noqa: E501
            # collection_formats['qcstatus'] = 'csv'  # noqa: E501
        if 'uploadstatus' in params:
            query_params.append(('uploadstatus', params['uploadstatus']))  # noqa: E501
            # collection_formats['uploadstatus'] = 'csv'  # noqa: E501
        if 'inputbiosamples' in params:
            query_params.append(('inputbiosamples', params['inputbiosamples']))  # noqa: E501
            # collection_formats['inputbiosamples'] = 'csv'  # noqa: E501
        if 'inputruns' in params:
            query_params.append(('inputruns', params['inputruns']))  # noqa: E501
            # collection_formats['inputruns'] = 'csv'  # noqa: E501
        if 'inputruntokens' in params:
            query_params.append(('inputruntokens', params['inputruntokens']))  # noqa: E501
            # collection_formats['inputruntokens'] = 'csv'  # noqa: E501
        if 'projectid' in params:
            query_params.append(('projectid', params['projectid']))  # noqa: E501
        if 'appsessionids' in params:
            query_params.append(('appsessionids', params['appsessionids']))  # noqa: E501
            # collection_formats['appsessionids'] = 'csv'  # noqa: E501
        if 'isarchived' in params:
            query_params.append(('isarchived', params['isarchived']))  # noqa: E501
        if 'sortby' in params:
            query_params.append(('sortby', params['sortby']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sortdir' in params:
            query_params.append(('sortdir', params['sortdir']))  # noqa: E501

        # form_params = []
        # local_var_files = {}
        # body_params = None
        # # HTTP header `Accept`
        # header_params['Accept'] = self.api_client.select_header_accept(
        #     ['application/json'])  # noqa: E501
        #
        # # HTTP header `Content-Type`
        # header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
        #     ['application/json'])  # noqa: E501

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        resource_path = '/datasets'
        method = 'GET'

        # Authentication setting
        # auth_settings = ['api_key', 'basespace_auth']  # noqa: E501

        # return self.api_client.call_api(
        #     '/datasets', 'GET',
        #     path_params,
        #     query_params,
        #     header_params,
        #     body=body_params,
        #     post_params=form_params,
        #     files=local_var_files,
        #     response_type='V2DatasetCompactList',  # noqa: E501
        #     auth_settings=auth_settings,
        #     async_req=params.get('async_req'),
        #     _return_http_data_only=params.get('_return_http_data_only'),
        #     _preload_content=params.get('_preload_content', True),
        #     _request_timeout=params.get('_request_timeout'),
        #     collection_formats=collection_formats)

        return self.api_client.callAPI(resource_path, method, dict(query_params), None, header_params)

    # def get_v2_datasets_id(self, id, **kwargs):  # noqa: E501
    #     """Get information about a dataset  # noqa: E501
    #
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.get_v2_datasets_id(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset ID (required)
    #     :return: V2Dataset
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #     kwargs['_return_http_data_only'] = True
    #     if kwargs.get('async_req'):
    #         return self.get_v2_datasets_id_with_http_info(id, **kwargs)  # noqa: E501
    #     else:
    #         (data) = self.get_v2_datasets_id_with_http_info(id, **kwargs)  # noqa: E501
    #         return data
    #
    # def get_v2_datasets_id_with_http_info(self, id, **kwargs):  # noqa: E501
    #     """Get information about a dataset  # noqa: E501
    #
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.get_v2_datasets_id_with_http_info(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset ID (required)
    #     :return: V2Dataset
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #
    #     all_params = ['id']  # noqa: E501
    #     all_params.append('async_req')
    #     all_params.append('_return_http_data_only')
    #     all_params.append('_preload_content')
    #     all_params.append('_request_timeout')
    #
    #     params = locals()
    #     for key, val in six.iteritems(params['kwargs']):
    #         if key not in all_params:
    #             raise TypeError(
    #                 "Got an unexpected keyword argument '%s'"
    #                 " to method get_v2_datasets_id" % key
    #             )
    #         params[key] = val
    #     del params['kwargs']
    #     # verify the required parameter 'id' is set
    #     if ''' self.api_client.client_side_validation '''('id' not in params or
    #                                                       params['id'] is None):  # noqa: E501
    #         raise ValueError("Missing the required parameter `id` when calling `get_v2_datasets_id`")  # noqa: E501
    #
    #     collection_formats = {}
    #
    #     path_params = {}
    #     if 'id' in params:
    #         path_params['id'] = params['id']  # noqa: E501
    #
    #     query_params = []
    #
    #     header_params = {}
    #
    #     form_params = []
    #     local_var_files = {}
    #
    #     body_params = None
    #     # HTTP header `Accept`
    #     header_params['Accept'] = self.api_client.select_header_accept(
    #         ['application/json'])  # noqa: E501
    #
    #     # HTTP header `Content-Type`
    #     header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
    #         ['application/json'])  # noqa: E501
    #
    #     # Authentication setting
    #     auth_settings = ['api_key', 'basespace_auth']  # noqa: E501
    #
    #     return self.api_client.call_api(
    #         '/datasets/{id}', 'GET',
    #         path_params,
    #         query_params,
    #         header_params,
    #         body=body_params,
    #         post_params=form_params,
    #         files=local_var_files,
    #         response_type='V2Dataset',  # noqa: E501
    #         auth_settings=auth_settings,
    #         async_req=params.get('async_req'),
    #         _return_http_data_only=params.get('_return_http_data_only'),
    #         _preload_content=params.get('_preload_content', True),
    #         _request_timeout=params.get('_request_timeout'),
    #         collection_formats=collection_formats)
    #
    # def get_v2_datasets_id_comments(self, id, **kwargs):  # noqa: E501
    #     """Get a list of comments made about a dataset  # noqa: E501
    #
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.get_v2_datasets_id_comments(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset ID (required)
    #     :param str sortby: The field(s) used to sort the result set
    #     :param int offset: The starting offset to read
    #     :param int limit: The maximum number of items to return
    #     :param str sortdir: The sort direction for the result set
    #     :return: V2CommentList
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #     kwargs['_return_http_data_only'] = True
    #     if kwargs.get('async_req'):
    #         return self.get_v2_datasets_id_comments_with_http_info(id, **kwargs)  # noqa: E501
    #     else:
    #         (data) = self.get_v2_datasets_id_comments_with_http_info(id, **kwargs)  # noqa: E501
    #         return data
    #
    # def get_v2_datasets_id_comments_with_http_info(self, id, **kwargs):  # noqa: E501
    #     """Get a list of comments made about a dataset  # noqa: E501
    #
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.get_v2_datasets_id_comments_with_http_info(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset ID (required)
    #     :param str sortby: The field(s) used to sort the result set
    #     :param int offset: The starting offset to read
    #     :param int limit: The maximum number of items to return
    #     :param str sortdir: The sort direction for the result set
    #     :return: V2CommentList
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #
    #     all_params = ['id', 'sortby', 'offset', 'limit', 'sortdir']  # noqa: E501
    #     all_params.append('async_req')
    #     all_params.append('_return_http_data_only')
    #     all_params.append('_preload_content')
    #     all_params.append('_request_timeout')
    #
    #     params = locals()
    #     for key, val in six.iteritems(params['kwargs']):
    #         if key not in all_params:
    #             raise TypeError(
    #                 "Got an unexpected keyword argument '%s'"
    #                 " to method get_v2_datasets_id_comments" % key
    #             )
    #         params[key] = val
    #     del params['kwargs']
    #     # verify the required parameter 'id' is set
    #     if ''' self.api_client.client_side_validation ''' and ('id' not in params or
    #                                                            params['id'] is None):  # noqa: E501
    #         raise ValueError(
    #             "Missing the required parameter `id` when calling `get_v2_datasets_id_comments`")  # noqa: E501
    #
    #     collection_formats = {}
    #
    #     path_params = {}
    #     if 'id' in params:
    #         path_params['id'] = params['id']  # noqa: E501
    #
    #     query_params = []
    #     if 'sortby' in params:
    #         query_params.append(('sortby', params['sortby']))  # noqa: E501
    #     if 'offset' in params:
    #         query_params.append(('offset', params['offset']))  # noqa: E501
    #     if 'limit' in params:
    #         query_params.append(('limit', params['limit']))  # noqa: E501
    #     if 'sortdir' in params:
    #         query_params.append(('sortdir', params['sortdir']))  # noqa: E501
    #
    #     header_params = {}
    #
    #     form_params = []
    #     local_var_files = {}
    #
    #     body_params = None
    #     # HTTP header `Accept`
    #     header_params['Accept'] = self.api_client.select_header_accept(
    #         ['application/json'])  # noqa: E501
    #
    #     # HTTP header `Content-Type`
    #     header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
    #         ['application/json'])  # noqa: E501
    #
    #     # Authentication setting
    #     auth_settings = ['api_key', 'basespace_auth']  # noqa: E501
    #
    #     return self.api_client.call_api(
    #         '/datasets/{id}/comments', 'GET',
    #         path_params,
    #         query_params,
    #         header_params,
    #         body=body_params,
    #         post_params=form_params,
    #         files=local_var_files,
    #         response_type='V2CommentList',  # noqa: E501
    #         auth_settings=auth_settings,
    #         async_req=params.get('async_req'),
    #         _return_http_data_only=params.get('_return_http_data_only'),
    #         _preload_content=params.get('_preload_content', True),
    #         _request_timeout=params.get('_request_timeout'),
    #         collection_formats=collection_formats)

    def get_v2_datasets_id_files(self, excludevcfindexfolder, excludebamcoveragefolder, excludesystemfolder,
                                 excludeemptyfiles, filehrefcontentresolution, turbomode, id, **kwargs):  # noqa: E501
        """Get a list of files of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_datasets_id_files(excludevcfindexfolder, excludebamcoveragefolder, excludesystemfolder, excludeemptyfiles, filehrefcontentresolution, turbomode, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool excludevcfindexfolder: Whether to exclude VCF index folders (required)
        :param bool excludebamcoveragefolder: Whether to exclude BAM coverage folders (required)
        :param bool excludesystemfolder: Whether to exclude system folders (required)
        :param bool excludeemptyfiles: Whether to exclude empty files (required)
        :param bool filehrefcontentresolution: Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content (required)
        :param bool turbomode: (required)
        :param str id: The Id of the resource (required)
        :param str filesetid:
        :param str extensions: Filter by file extension
        :param str excludeextensions: Exclude by file extension
        :param str directory: Filter by directory path (root is /)
        :param bool includesubdirectories: Whether to return subdirectories
        :param list[str] statuses: Optionally filter by status (default complete)
        :param str pathprefix: To be pre-fixed in the path of the file
        :param str sortby: The field(s) used to sort the result set
        :param int offset: The starting offset to read
        :param int limit: The maximum number of items to return
        :param str sortdir: The sort direction for the result set
        :return: V2FilesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v2_datasets_id_files_with_http_info(excludevcfindexfolder, excludebamcoveragefolder,
                                                                excludesystemfolder, excludeemptyfiles,
                                                                filehrefcontentresolution, turbomode, id,
                                                                **kwargs)  # noqa: E501
        else:
            (data) = self.get_v2_datasets_id_files_with_http_info(excludevcfindexfolder, excludebamcoveragefolder,
                                                                  excludesystemfolder, excludeemptyfiles,
                                                                  filehrefcontentresolution, turbomode, id,
                                                                  **kwargs)  # noqa: E501
            return data

    def get_v2_datasets_id_files_with_http_info(self, excludevcfindexfolder, excludebamcoveragefolder,
                                                excludesystemfolder, excludeemptyfiles, filehrefcontentresolution,
                                                turbomode, id, **kwargs):  # noqa: E501
        """Get a list of files of a dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_datasets_id_files_with_http_info(excludevcfindexfolder, excludebamcoveragefolder, excludesystemfolder, excludeemptyfiles, filehrefcontentresolution, turbomode, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool excludevcfindexfolder: Whether to exclude VCF index folders (required)
        :param bool excludebamcoveragefolder: Whether to exclude BAM coverage folders (required)
        :param bool excludesystemfolder: Whether to exclude system folders (required)
        :param bool excludeemptyfiles: Whether to exclude empty files (required)
        :param bool filehrefcontentresolution: Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content (required)
        :param bool turbomode: (required)
        :param str id: The Id of the resource (required)
        :param str filesetid:
        :param str extensions: Filter by file extension
        :param str excludeextensions: Exclude by file extension
        :param str directory: Filter by directory path (root is /)
        :param bool includesubdirectories: Whether to return subdirectories
        :param list[str] statuses: Optionally filter by status (default complete)
        :param str pathprefix: To be pre-fixed in the path of the file
        :param str sortby: The field(s) used to sort the result set
        :param int offset: The starting offset to read
        :param int limit: The maximum number of items to return
        :param str sortdir: The sort direction for the result set
        :return: V2FilesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['excludevcfindexfolder', 'excludebamcoveragefolder', 'excludesystemfolder', 'excludeemptyfiles',
                      'filehrefcontentresolution', 'turbomode', 'id', 'filesetid', 'extensions', 'excludeextensions',
                      'directory', 'includesubdirectories', 'statuses', 'pathprefix', 'sortby', 'offset', 'limit',
                      'sortdir']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v2_datasets_id_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'excludevcfindexfolder' is set
        if ''' self.api_client.client_side_validation ''' and ('excludevcfindexfolder' not in params or
                                                               params['excludevcfindexfolder'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `excludevcfindexfolder` when calling `get_v2_datasets_id_files`")  # noqa: E501
        # verify the required parameter 'excludebamcoveragefolder' is set
        if ''' self.api_client.client_side_validation ''' and ('excludebamcoveragefolder' not in params or
                                                               params[
                                                                   'excludebamcoveragefolder'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `excludebamcoveragefolder` when calling `get_v2_datasets_id_files`")  # noqa: E501
        # verify the required parameter 'excludesystemfolder' is set
        if ''' self.api_client.client_side_validation ''' and ('excludesystemfolder' not in params or
                                                               params['excludesystemfolder'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `excludesystemfolder` when calling `get_v2_datasets_id_files`")  # noqa: E501
        # verify the required parameter 'excludeemptyfiles' is set
        if ''' self.api_client.client_side_validation ''' and ('excludeemptyfiles' not in params or
                                                               params['excludeemptyfiles'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `excludeemptyfiles` when calling `get_v2_datasets_id_files`")  # noqa: E501
        # verify the required parameter 'filehrefcontentresolution' is set
        if ''' self.api_client.client_side_validation ''' and ('filehrefcontentresolution' not in params or
                                                               params[
                                                                   'filehrefcontentresolution'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `filehrefcontentresolution` when calling `get_v2_datasets_id_files`")  # noqa: E501
        # verify the required parameter 'turbomode' is set
        if ''' self.api_client.client_side_validation ''' and ('turbomode' not in params or
                                                               params['turbomode'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `turbomode` when calling `get_v2_datasets_id_files`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ''' self.api_client.client_side_validation ''' and ('id' not in params or
                                                               params['id'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `get_v2_datasets_id_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'filesetid' in params:
            query_params.append(('filesetid', params['filesetid']))  # noqa: E501
        if 'extensions' in params:
            query_params.append(('extensions', params['extensions']))  # noqa: E501
        if 'excludeextensions' in params:
            query_params.append(('excludeextensions', params['excludeextensions']))  # noqa: E501
        if 'directory' in params:
            query_params.append(('directory', params['directory']))  # noqa: E501
        if 'includesubdirectories' in params:
            query_params.append(('includesubdirectories', params['includesubdirectories']))  # noqa: E501
        if 'excludevcfindexfolder' in params:
            query_params.append(('excludevcfindexfolder', params['excludevcfindexfolder']))  # noqa: E501
        if 'excludebamcoveragefolder' in params:
            query_params.append(('excludebamcoveragefolder', params['excludebamcoveragefolder']))  # noqa: E501
        if 'excludesystemfolder' in params:
            query_params.append(('excludesystemfolder', params['excludesystemfolder']))  # noqa: E501
        if 'excludeemptyfiles' in params:
            query_params.append(('excludeemptyfiles', params['excludeemptyfiles']))  # noqa: E501
        if 'filehrefcontentresolution' in params:
            query_params.append(('filehrefcontentresolution', params['filehrefcontentresolution']))  # noqa: E501
        if 'statuses' in params:
            query_params.append(('statuses', params['statuses']))  # noqa: E501
            collection_formats['statuses'] = 'csv'  # noqa: E501
        if 'turbomode' in params:
            query_params.append(('turbomode', params['turbomode']))  # noqa: E501
        if 'pathprefix' in params:
            query_params.append(('pathprefix', params['pathprefix']))  # noqa: E501
        if 'sortby' in params:
            query_params.append(('sortby', params['sortby']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sortdir' in params:
            query_params.append(('sortdir', params['sortdir']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # # HTTP header `Accept`
        # header_params['Accept'] = self.api_client.select_header_accept(
        #     ['application/json'])  # noqa: E501
        #
        # # HTTP header `Content-Type`
        # header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
        #     ['application/json'])  # noqa: E501

        # AttributeError: 'APIClient' object has no attribute 'select_header_accept'
        # YF - I comment code above to this:
        header_params['Accept'] = 'application/json'
        header_params['Content-Type'] = 'application/json'

        resourcePath = f'/datasets/{id}/files'
        method = 'GET'

        # Authentication setting
        # auth_settings = ['api_key', 'basespace_auth']  # noqa: E501

        return self.api_client.callAPI(resourcePath, method, dict(query_params), None, header_params)
        # return self.api_client.call_api(
        #     '/datasets/{id}/files', 'GET',
        #     path_params,
        #     query_params,
        #     header_params,
        #     body=body_params,
        #     post_params=form_params,
        #     files=local_var_files,
        #     response_type='V2FilesList',  # noqa: E501
        #     auth_settings=auth_settings,
        #     async_req=params.get('async_req'),
        #     _return_http_data_only=params.get('_return_http_data_only'),
        #     _preload_content=params.get('_preload_content', True),
        #     _request_timeout=params.get('_request_timeout'),
        #     collection_formats=collection_formats)

    # def get_v2_datasettypes_id(self, id, **kwargs):  # noqa: E501
    #     """Get information about a dataset type  # noqa: E501
    #
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.get_v2_datasettypes_id(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset type ID (required)
    #     :param list[str] include:
    #     :return: V2DatasetType
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #     kwargs['_return_http_data_only'] = True
    #     if kwargs.get('async_req'):
    #         return self.get_v2_datasettypes_id_with_http_info(id, **kwargs)  # noqa: E501
    #     else:
    #         (data) = self.get_v2_datasettypes_id_with_http_info(id, **kwargs)  # noqa: E501
    #         return data
    #
    # def get_v2_datasettypes_id_with_http_info(self, id, **kwargs):  # noqa: E501
    #     """Get information about a dataset type  # noqa: E501
    #
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.get_v2_datasettypes_id_with_http_info(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset type ID (required)
    #     :param list[str] include:
    #     :return: V2DatasetType
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #
    #     all_params = ['id', 'include']  # noqa: E501
    #     all_params.append('async_req')
    #     all_params.append('_return_http_data_only')
    #     all_params.append('_preload_content')
    #     all_params.append('_request_timeout')
    #
    #     params = locals()
    #     for key, val in six.iteritems(params['kwargs']):
    #         if key not in all_params:
    #             raise TypeError(
    #                 "Got an unexpected keyword argument '%s'"
    #                 " to method get_v2_datasettypes_id" % key
    #             )
    #         params[key] = val
    #     del params['kwargs']
    #     # verify the required parameter 'id' is set
    #     if ''' self.api_client.client_side_validation ''' and ('id' not in params or
    #                                                            params['id'] is None):  # noqa: E501
    #         raise ValueError("Missing the required parameter `id` when calling `get_v2_datasettypes_id`")  # noqa: E501
    #
    #     collection_formats = {}
    #
    #     path_params = {}
    #     if 'id' in params:
    #         path_params['id'] = params['id']  # noqa: E501
    #
    #     query_params = []
    #     if 'include' in params:
    #         query_params.append(('include', params['include']))  # noqa: E501
    #         collection_formats['include'] = 'csv'  # noqa: E501
    #
    #     header_params = {}
    #
    #     form_params = []
    #     local_var_files = {}
    #
    #     body_params = None
    #     # HTTP header `Accept`
    #     header_params['Accept'] = self.api_client.select_header_accept(
    #         ['application/json'])  # noqa: E501
    #
    #     # HTTP header `Content-Type`
    #     header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
    #         ['application/json'])  # noqa: E501
    #
    #     # Authentication setting
    #     auth_settings = ['api_key', 'basespace_auth']  # noqa: E501
    #
    #     return self.api_client.call_api(
    #         '/datasettypes/{id}', 'GET',
    #         path_params,
    #         query_params,
    #         header_params,
    #         body=body_params,
    #         post_params=form_params,
    #         files=local_var_files,
    #         response_type='V2DatasetType',  # noqa: E501
    #         auth_settings=auth_settings,
    #         async_req=params.get('async_req'),
    #         _return_http_data_only=params.get('_return_http_data_only'),
    #         _preload_content=params.get('_preload_content', True),
    #         _request_timeout=params.get('_request_timeout'),
    #         collection_formats=collection_formats)
    #
    # def post_v2_datasets_id(self, id, **kwargs):  # noqa: E501
    #     """Update an existing dataset  # noqa: E501
    #
    #     The QcStatus of a dataset may only be updated when the UploadStatus is set to “Complete”. The QcStatus may then be updated to one of the following values: QcFailed or QcPassed. A comment may be entered into the Comment field when updating the dataset QcStatus.  # noqa: E501
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.post_v2_datasets_id(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset ID (required)
    #     :param V2PostDatasetsIdRequest payload:
    #     :return: V2Dataset
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #     kwargs['_return_http_data_only'] = True
    #     if kwargs.get('async_req'):
    #         return self.post_v2_datasets_id_with_http_info(id, **kwargs)  # noqa: E501
    #     else:
    #         (data) = self.post_v2_datasets_id_with_http_info(id, **kwargs)  # noqa: E501
    #         return data
    #
    # def post_v2_datasets_id_with_http_info(self, id, **kwargs):  # noqa: E501
    #     """Update an existing dataset  # noqa: E501
    #
    #     The QcStatus of a dataset may only be updated when the UploadStatus is set to “Complete”. The QcStatus may then be updated to one of the following values: QcFailed or QcPassed. A comment may be entered into the Comment field when updating the dataset QcStatus.  # noqa: E501
    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.post_v2_datasets_id_with_http_info(id, async_req=True)
    #     >>> result = thread.get()
    #
    #     :param async_req bool
    #     :param str id: Dataset ID (required)
    #     :param V2PostDatasetsIdRequest payload:
    #     :return: V2Dataset
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #
    #     all_params = ['id', 'payload']  # noqa: E501
    #     all_params.append('async_req')
    #     all_params.append('_return_http_data_only')
    #     all_params.append('_preload_content')
    #     all_params.append('_request_timeout')
    #
    #     params = locals()
    #     for key, val in six.iteritems(params['kwargs']):
    #         if key not in all_params:
    #             raise TypeError(
    #                 "Got an unexpected keyword argument '%s'"
    #                 " to method post_v2_datasets_id" % key
    #             )
    #         params[key] = val
    #     del params['kwargs']
    #     # verify the required parameter 'id' is set
    #     if ''' self.api_client.client_side_validation ''' and ('id' not in params or
    #                                                            params['id'] is None):  # noqa: E501
    #         raise ValueError("Missing the required parameter `id` when calling `post_v2_datasets_id`")  # noqa: E501
    #
    #     collection_formats = {}
    #
    #     path_params = {}
    #     if 'id' in params:
    #         path_params['id'] = params['id']  # noqa: E501
    #
    #     query_params = []
    #
    #     header_params = {}
    #
    #     form_params = []
    #     local_var_files = {}
    #
    #     body_params = None
    #     if 'payload' in params:
    #         body_params = params['payload']
    #     # HTTP header `Accept`
    #     header_params['Accept'] = self.api_client.select_header_accept(
    #         ['application/json'])  # noqa: E501
    #
    #     # HTTP header `Content-Type`
    #     header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
    #         ['application/json'])  # noqa: E501
    #
    #     # Authentication setting
    #     auth_settings = ['api_key', 'basespace_auth']  # noqa: E501
    #
    #     return self.api_client.call_api(
    #         '/datasets/{id}', 'POST',
    #         path_params,
    #         query_params,
    #         header_params,
    #         body=body_params,
    #         post_params=form_params,
    #         files=local_var_files,
    #         response_type='V2Dataset',  # noqa: E501
    #         auth_settings=auth_settings,
    #         async_req=params.get('async_req'),
    #         _return_http_data_only=params.get('_return_http_data_only'),
    #         _preload_content=params.get('_preload_content', True),
    #         _request_timeout=params.get('_request_timeout'),
    #         collection_formats=collection_formats)
