# coding: utf-8

"""
    Basespace API

    Basespace REST API  # noqa: E501

    OpenAPI spec version: 5.0.0
"""


import pprint
import re  # noqa: F401

import six

from BaseSpacePy.configuration import Configuration


class V2DatasetCompact(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'href': 'str',
        'href_files': 'str',
        'href_base_space_ui': 'str',
        'name': 'str',
        'date_created': 'datetime',
        'date_modified': 'datetime',
        'app_session': 'V2AppSessionCompact',
        'project': 'V1pre3ProjectCompact',
        'total_size': 'int',
        'is_deleted': 'bool',
        'is_archived': 'bool',
        'is_file_data_deleted': 'bool',
        'user_owned_by': 'V1pre3UserCompact',
        'dataset_type': 'V2DatasetTypeCompact',
        'properties': 'V2PropertyContainer',
        'qc_status': 'str',
        'qc_status_summary': 'str',
        'upload_status': 'str',
        'upload_status_summary': 'str',
        'validation_status': 'str',
        'v1pre3_id': 'str',
        'href_comments': 'str',
        'contains_comments': 'bool',
        'origin_dataset': 'V2DatasetCompact'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'href_files': 'HrefFiles',
        'href_base_space_ui': 'HrefBaseSpaceUI',
        'name': 'Name',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified',
        'app_session': 'AppSession',
        'project': 'Project',
        'total_size': 'TotalSize',
        'is_deleted': 'IsDeleted',
        'is_archived': 'IsArchived',
        'is_file_data_deleted': 'IsFileDataDeleted',
        'user_owned_by': 'UserOwnedBy',
        'dataset_type': 'DatasetType',
        'properties': 'Properties',
        'qc_status': 'QcStatus',
        'qc_status_summary': 'QcStatusSummary',
        'upload_status': 'UploadStatus',
        'upload_status_summary': 'UploadStatusSummary',
        'validation_status': 'ValidationStatus',
        'v1pre3_id': 'V1pre3Id',
        'href_comments': 'HrefComments',
        'contains_comments': 'ContainsComments',
        'origin_dataset': 'OriginDataset'
    }

    def __init__(self, id=None, href=None, href_files=None, href_base_space_ui=None, name=None, date_created=None, date_modified=None, app_session=None, project=None, total_size=None, is_deleted=None, is_archived=None, is_file_data_deleted=None, user_owned_by=None, dataset_type=None, properties=None, qc_status=None, qc_status_summary=None, upload_status=None, upload_status_summary=None, validation_status=None, v1pre3_id=None, href_comments=None, contains_comments=None, origin_dataset=None, _configuration=None):  # noqa: E501
        """V2DatasetCompact - a model defined for a DataSet object representation"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._href = None
        self._href_files = None
        self._href_base_space_ui = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._app_session = None
        self._project = None
        self._total_size = None
        self._is_deleted = None
        self._is_archived = None
        self._is_file_data_deleted = None
        self._user_owned_by = None
        self._dataset_type = None
        self._properties = None
        self._qc_status = None
        self._qc_status_summary = None
        self._upload_status = None
        self._upload_status_summary = None
        self._validation_status = None
        self._v1pre3_id = None
        self._href_comments = None
        self._contains_comments = None
        self._origin_dataset = None
        self.discriminator = None

        self.id = id
        self.href = href
        self.href_files = href_files
        self.href_base_space_ui = href_base_space_ui
        self.name = name
        self.date_created = date_created
        self.date_modified = date_modified
        self.app_session = app_session
        self.project = project
        self.total_size = total_size
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_archived is not None:
            self.is_archived = is_archived
        if is_file_data_deleted is not None:
            self.is_file_data_deleted = is_file_data_deleted
        self.user_owned_by = user_owned_by
        self.dataset_type = dataset_type
        self.properties = properties
        self.qc_status = qc_status
        self.qc_status_summary = qc_status_summary
        self.upload_status = upload_status
        self.upload_status_summary = upload_status_summary
        self.validation_status = validation_status
        self.v1pre3_id = v1pre3_id
        self.href_comments = href_comments
        self.contains_comments = contains_comments
        self.origin_dataset = origin_dataset

    @property
    def id(self):
        """Gets the id of this V2DatasetCompact.  # noqa: E501


        :return: The id of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2DatasetCompact.


        :param id: The id of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def Id(self):
        """Gets the id of this V2DatasetCompact.  # noqa: E501


        :return: The id of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @property
    def Name(self):
        """Gets the id of this V2DatasetCompact.  # noqa: E501


        :return: The id of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._name



    @property
    def href(self):
        """Gets the href of this V2DatasetCompact.  # noqa: E501


        :return: The href of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2DatasetCompact.


        :param href: The href of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def href_files(self):
        """Gets the href_files of this V2DatasetCompact.  # noqa: E501


        :return: The href_files of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_files

    @href_files.setter
    def href_files(self, href_files):
        """Sets the href_files of this V2DatasetCompact.


        :param href_files: The href_files of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href_files is None:
            raise ValueError("Invalid value for `href_files`, must not be `None`")  # noqa: E501

        self._href_files = href_files

    @property
    def href_base_space_ui(self):
        """Gets the href_base_space_ui of this V2DatasetCompact.  # noqa: E501


        :return: The href_base_space_ui of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_base_space_ui

    @href_base_space_ui.setter
    def href_base_space_ui(self, href_base_space_ui):
        """Sets the href_base_space_ui of this V2DatasetCompact.


        :param href_base_space_ui: The href_base_space_ui of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        # if self._configuration.client_side_validation and href_base_space_ui is None:
        #     raise ValueError("Invalid value for `href_base_space_ui`, must not be `None`")  # noqa: E501

        self._href_base_space_ui = href_base_space_ui

    @property
    def name(self):
        """Gets the name of this V2DatasetCompact.  # noqa: E501


        :return: The name of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2DatasetCompact.


        :param name: The name of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def date_created(self):
        """Gets the date_created of this V2DatasetCompact.  # noqa: E501


        :return: The date_created of this V2DatasetCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this V2DatasetCompact.


        :param date_created: The date_created of this V2DatasetCompact.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this V2DatasetCompact.  # noqa: E501


        :return: The date_modified of this V2DatasetCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this V2DatasetCompact.


        :param date_modified: The date_modified of this V2DatasetCompact.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and date_modified is None:
            raise ValueError("Invalid value for `date_modified`, must not be `None`")  # noqa: E501

        self._date_modified = date_modified

    @property
    def app_session(self):
        """Gets the app_session of this V2DatasetCompact.  # noqa: E501


        :return: The app_session of this V2DatasetCompact.  # noqa: E501
        :rtype: V2AppSessionCompact
        """
        return self._app_session

    @app_session.setter
    def app_session(self, app_session):
        """Sets the app_session of this V2DatasetCompact.


        :param app_session: The app_session of this V2DatasetCompact.  # noqa: E501
        :type: V2AppSessionCompact
        """
        if self._configuration.client_side_validation and app_session is None:
            raise ValueError("Invalid value for `app_session`, must not be `None`")  # noqa: E501

        self._app_session = app_session

    @property
    def project(self):
        """Gets the project of this V2DatasetCompact.  # noqa: E501


        :return: The project of this V2DatasetCompact.  # noqa: E501
        :rtype: V1pre3ProjectCompact
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V2DatasetCompact.


        :param project: The project of this V2DatasetCompact.  # noqa: E501
        :type: V1pre3ProjectCompact
        """
        if self._configuration.client_side_validation and project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def total_size(self):
        """Gets the total_size of this V2DatasetCompact.  # noqa: E501


        :return: The total_size of this V2DatasetCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this V2DatasetCompact.


        :param total_size: The total_size of this V2DatasetCompact.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_size is None:
            raise ValueError("Invalid value for `total_size`, must not be `None`")  # noqa: E501

        self._total_size = total_size

    @property
    def is_deleted(self):
        """Gets the is_deleted of this V2DatasetCompact.  # noqa: E501


        :return: The is_deleted of this V2DatasetCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this V2DatasetCompact.


        :param is_deleted: The is_deleted of this V2DatasetCompact.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def is_archived(self):
        """Gets the is_archived of this V2DatasetCompact.  # noqa: E501


        :return: The is_archived of this V2DatasetCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this V2DatasetCompact.


        :param is_archived: The is_archived of this V2DatasetCompact.  # noqa: E501
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_file_data_deleted(self):
        """Gets the is_file_data_deleted of this V2DatasetCompact.  # noqa: E501


        :return: The is_file_data_deleted of this V2DatasetCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_file_data_deleted

    @is_file_data_deleted.setter
    def is_file_data_deleted(self, is_file_data_deleted):
        """Sets the is_file_data_deleted of this V2DatasetCompact.


        :param is_file_data_deleted: The is_file_data_deleted of this V2DatasetCompact.  # noqa: E501
        :type: bool
        """

        self._is_file_data_deleted = is_file_data_deleted

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this V2DatasetCompact.  # noqa: E501


        :return: The user_owned_by of this V2DatasetCompact.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this V2DatasetCompact.


        :param user_owned_by: The user_owned_by of this V2DatasetCompact.  # noqa: E501
        :type: V1pre3UserCompact
        """
        if self._configuration.client_side_validation and user_owned_by is None:
            raise ValueError("Invalid value for `user_owned_by`, must not be `None`")  # noqa: E501

        self._user_owned_by = user_owned_by

    @property
    def dataset_type(self):
        """Gets the dataset_type of this V2DatasetCompact.  # noqa: E501


        :return: The dataset_type of this V2DatasetCompact.  # noqa: E501
        :rtype: V2DatasetTypeCompact
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        """Sets the dataset_type of this V2DatasetCompact.


        :param dataset_type: The dataset_type of this V2DatasetCompact.  # noqa: E501
        :type: V2DatasetTypeCompact
        """
        if self._configuration.client_side_validation and dataset_type is None:
            raise ValueError("Invalid value for `dataset_type`, must not be `None`")  # noqa: E501

        self._dataset_type = dataset_type

    @property
    def properties(self):
        """Gets the properties of this V2DatasetCompact.  # noqa: E501


        :return: The properties of this V2DatasetCompact.  # noqa: E501
        :rtype: V2PropertyContainer
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V2DatasetCompact.


        :param properties: The properties of this V2DatasetCompact.  # noqa: E501
        :type: V2PropertyContainer
        """
        if self._configuration.client_side_validation and properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def qc_status(self):
        """Gets the qc_status of this V2DatasetCompact.  # noqa: E501


        :return: The qc_status of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._qc_status

    @qc_status.setter
    def qc_status(self, qc_status):
        """Sets the qc_status of this V2DatasetCompact.


        :param qc_status: The qc_status of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and qc_status is None:
            raise ValueError("Invalid value for `qc_status`, must not be `None`")  # noqa: E501

        self._qc_status = qc_status

    @property
    def qc_status_summary(self):
        """Gets the qc_status_summary of this V2DatasetCompact.  # noqa: E501


        :return: The qc_status_summary of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._qc_status_summary

    @qc_status_summary.setter
    def qc_status_summary(self, qc_status_summary):
        """Sets the qc_status_summary of this V2DatasetCompact.


        :param qc_status_summary: The qc_status_summary of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and qc_status_summary is None:
            raise ValueError("Invalid value for `qc_status_summary`, must not be `None`")  # noqa: E501

        self._qc_status_summary = qc_status_summary

    @property
    def upload_status(self):
        """Gets the upload_status of this V2DatasetCompact.  # noqa: E501


        :return: The upload_status of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status):
        """Sets the upload_status of this V2DatasetCompact.


        :param upload_status: The upload_status of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and upload_status is None:
            raise ValueError("Invalid value for `upload_status`, must not be `None`")  # noqa: E501

        self._upload_status = upload_status

    @property
    def upload_status_summary(self):
        """Gets the upload_status_summary of this V2DatasetCompact.  # noqa: E501


        :return: The upload_status_summary of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._upload_status_summary

    @upload_status_summary.setter
    def upload_status_summary(self, upload_status_summary):
        """Sets the upload_status_summary of this V2DatasetCompact.


        :param upload_status_summary: The upload_status_summary of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and upload_status_summary is None:
            raise ValueError("Invalid value for `upload_status_summary`, must not be `None`")  # noqa: E501

        self._upload_status_summary = upload_status_summary

    @property
    def validation_status(self):
        """Gets the validation_status of this V2DatasetCompact.  # noqa: E501


        :return: The validation_status of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """Sets the validation_status of this V2DatasetCompact.


        :param validation_status: The validation_status of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        # if self._configuration.client_side_validation and validation_status is None:
        #     raise ValueError("Invalid value for `validation_status`, must not be `None`")  # noqa: E501

        self._validation_status = validation_status

    @property
    def v1pre3_id(self):
        """Gets the v1pre3_id of this V2DatasetCompact.  # noqa: E501


        :return: The v1pre3_id of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._v1pre3_id

    @v1pre3_id.setter
    def v1pre3_id(self, v1pre3_id):
        """Sets the v1pre3_id of this V2DatasetCompact.


        :param v1pre3_id: The v1pre3_id of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and v1pre3_id is None:
            raise ValueError("Invalid value for `v1pre3_id`, must not be `None`")  # noqa: E501

        self._v1pre3_id = v1pre3_id

    @property
    def href_comments(self):
        """Gets the href_comments of this V2DatasetCompact.  # noqa: E501


        :return: The href_comments of this V2DatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_comments

    @href_comments.setter
    def href_comments(self, href_comments):
        """Sets the href_comments of this V2DatasetCompact.


        :param href_comments: The href_comments of this V2DatasetCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href_comments is None:
            raise ValueError("Invalid value for `href_comments`, must not be `None`")  # noqa: E501

        self._href_comments = href_comments

    @property
    def contains_comments(self):
        """Gets the contains_comments of this V2DatasetCompact.  # noqa: E501


        :return: The contains_comments of this V2DatasetCompact.  # noqa: E501
        :rtype: bool
        """
        return self._contains_comments

    @contains_comments.setter
    def contains_comments(self, contains_comments):
        """Sets the contains_comments of this V2DatasetCompact.


        :param contains_comments: The contains_comments of this V2DatasetCompact.  # noqa: E501
        :type: bool
        """
        # if self._configuration.client_side_validation and contains_comments is None:
        #     raise ValueError("Invalid value for `contains_comments`, must not be `None`")  # noqa: E501

        self._contains_comments = contains_comments

    @property
    def origin_dataset(self):
        """Gets the origin_dataset of this V2DatasetCompact.  # noqa: E501


        :return: The origin_dataset of this V2DatasetCompact.  # noqa: E501
        :rtype: V2DatasetCompact
        """
        return self._origin_dataset

    @origin_dataset.setter
    def origin_dataset(self, origin_dataset):
        """Sets the origin_dataset of this V2DatasetCompact.


        :param origin_dataset: The origin_dataset of this V2DatasetCompact.  # noqa: E501
        :type: V2DatasetCompact
        """
        # if self._configuration.client_side_validation and origin_dataset is None:
        #     raise ValueError("Invalid value for `origin_dataset`, must not be `None`")  # noqa: E501

        self._origin_dataset = origin_dataset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V2DatasetCompact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2DatasetCompact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2DatasetCompact):
            return True

        return self.to_dict() != other.to_dict()
