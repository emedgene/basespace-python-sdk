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


class V1pre3FileCompact(object):
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
        'href_content': 'str',
        'name': 'str',
        'content_type': 'str',
        'size': 'int',
        'path': 'str',
        'is_archived': 'bool',
        'date_created': 'datetime',
        'date_modified': 'datetime',
        'parent_sample': 'SampleCompact',
        'parent_app_result': 'V1pre3AppResultCompact',
        'parent_run': 'V1pre3RunCompact',
        'parent_genome': 'GenomeCompact',
        'parent_app_session': 'AppSessionCompact',
        'parent_projects': 'list[V1pre3ProjectCompact]',
        'category': 'str',
        'e_tag': 'str',
        'parent_dataset': 'V2DatasetCompact',
        'parent_project': 'IProjectCompact'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'href_content': 'HrefContent',
        'name': 'Name',
        'content_type': 'ContentType',
        'size': 'Size',
        'path': 'Path',
        'is_archived': 'IsArchived',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified',
        'parent_sample': 'ParentSample',
        'parent_app_result': 'ParentAppResult',
        'parent_run': 'ParentRun',
        'parent_genome': 'ParentGenome',
        'parent_app_session': 'ParentAppSession',
        'parent_projects': 'ParentProjects',
        'category': 'Category',
        'e_tag': 'ETag',
        'parent_dataset': 'ParentDataset',
        'parent_project': 'ParentProject'
    }

    def __init__(self, id=None, href=None, href_content=None, name=None, content_type=None, size=None, path=None, is_archived=None, date_created=None, date_modified=None, parent_sample=None, parent_app_result=None, parent_run=None, parent_genome=None, parent_app_session=None, parent_projects=None, category=None, e_tag=None, parent_dataset=None, parent_project=None, _configuration=None):  # noqa: E501
        """V1pre3FileCompact - a model defined for a file representation"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._href = None
        self._href_content = None
        self._name = None
        self._content_type = None
        self._size = None
        self._path = None
        self._is_archived = None
        self._date_created = None
        self._date_modified = None
        self._parent_sample = None
        self._parent_app_result = None
        self._parent_run = None
        self._parent_genome = None
        self._parent_app_session = None
        self._parent_projects = None
        self._category = None
        self._e_tag = None
        self._parent_dataset = None
        self._parent_project = None
        self.discriminator = None

        self.id = id
        self.href = href
        if href_content is not None:
            self.href_content = href_content
        if name is not None:
            self.name = name
        if content_type is not None:
            self.content_type = content_type
        if size is not None:
            self.size = size
        if path is not None:
            self.path = path
        if is_archived is not None:
            self.is_archived = is_archived
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified
        if parent_sample is not None:
            self.parent_sample = parent_sample
        if parent_app_result is not None:
            self.parent_app_result = parent_app_result
        if parent_run is not None:
            self.parent_run = parent_run
        if parent_genome is not None:
            self.parent_genome = parent_genome
        if parent_app_session is not None:
            self.parent_app_session = parent_app_session
        if parent_projects is not None:
            self.parent_projects = parent_projects
        if category is not None:
            self.category = category
        if e_tag is not None:
            self.e_tag = e_tag
        if parent_dataset is not None:
            self.parent_dataset = parent_dataset
        if parent_project is not None:
            self.parent_project = parent_project

    @property
    def id(self):
        """Gets the id of this V1pre3FileCompact.  # noqa: E501


        :return: The id of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1pre3FileCompact.


        :param id: The id of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def Id(self):
        """Gets the id of this V1pre3FileCompact.  # noqa: E501


        :return: The id of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @property
    def Name(self):
        """Gets the id of this V1pre3FileCompact.  # noqa: E501


        :return: The id of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._name


    @property
    def href(self):
        """Gets the href of this V1pre3FileCompact.  # noqa: E501


        :return: The href of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V1pre3FileCompact.


        :param href: The href of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def href_content(self):
        """Gets the href_content of this V1pre3FileCompact.  # noqa: E501


        :return: The href_content of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_content

    @href_content.setter
    def href_content(self, href_content):
        """Sets the href_content of this V1pre3FileCompact.


        :param href_content: The href_content of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """

        self._href_content = href_content

    @property
    def name(self):
        """Gets the name of this V1pre3FileCompact.  # noqa: E501


        :return: The name of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1pre3FileCompact.


        :param name: The name of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def content_type(self):
        """Gets the content_type of this V1pre3FileCompact.  # noqa: E501


        :return: The content_type of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this V1pre3FileCompact.


        :param content_type: The content_type of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def size(self):
        """Gets the size of this V1pre3FileCompact.  # noqa: E501


        :return: The size of this V1pre3FileCompact.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1pre3FileCompact.


        :param size: The size of this V1pre3FileCompact.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def path(self):
        """Gets the path of this V1pre3FileCompact.  # noqa: E501


        :return: The path of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1pre3FileCompact.


        :param path: The path of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def is_archived(self):
        """Gets the is_archived of this V1pre3FileCompact.  # noqa: E501


        :return: The is_archived of this V1pre3FileCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this V1pre3FileCompact.


        :param is_archived: The is_archived of this V1pre3FileCompact.  # noqa: E501
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def date_created(self):
        """Gets the date_created of this V1pre3FileCompact.  # noqa: E501


        :return: The date_created of this V1pre3FileCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this V1pre3FileCompact.


        :param date_created: The date_created of this V1pre3FileCompact.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this V1pre3FileCompact.  # noqa: E501


        :return: The date_modified of this V1pre3FileCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this V1pre3FileCompact.


        :param date_modified: The date_modified of this V1pre3FileCompact.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def parent_sample(self):
        """Gets the parent_sample of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_sample of this V1pre3FileCompact.  # noqa: E501
        :rtype: SampleCompact
        """
        return self._parent_sample

    @parent_sample.setter
    def parent_sample(self, parent_sample):
        """Sets the parent_sample of this V1pre3FileCompact.


        :param parent_sample: The parent_sample of this V1pre3FileCompact.  # noqa: E501
        :type: SampleCompact
        """

        self._parent_sample = parent_sample

    @property
    def parent_app_result(self):
        """Gets the parent_app_result of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_app_result of this V1pre3FileCompact.  # noqa: E501
        :rtype: V1pre3AppResultCompact
        """
        return self._parent_app_result

    @parent_app_result.setter
    def parent_app_result(self, parent_app_result):
        """Sets the parent_app_result of this V1pre3FileCompact.


        :param parent_app_result: The parent_app_result of this V1pre3FileCompact.  # noqa: E501
        :type: V1pre3AppResultCompact
        """

        self._parent_app_result = parent_app_result

    @property
    def parent_run(self):
        """Gets the parent_run of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_run of this V1pre3FileCompact.  # noqa: E501
        :rtype: V1pre3RunCompact
        """
        return self._parent_run

    @parent_run.setter
    def parent_run(self, parent_run):
        """Sets the parent_run of this V1pre3FileCompact.


        :param parent_run: The parent_run of this V1pre3FileCompact.  # noqa: E501
        :type: V1pre3RunCompact
        """

        self._parent_run = parent_run

    @property
    def parent_genome(self):
        """Gets the parent_genome of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_genome of this V1pre3FileCompact.  # noqa: E501
        :rtype: GenomeCompact
        """
        return self._parent_genome

    @parent_genome.setter
    def parent_genome(self, parent_genome):
        """Sets the parent_genome of this V1pre3FileCompact.


        :param parent_genome: The parent_genome of this V1pre3FileCompact.  # noqa: E501
        :type: GenomeCompact
        """

        self._parent_genome = parent_genome

    @property
    def parent_app_session(self):
        """Gets the parent_app_session of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_app_session of this V1pre3FileCompact.  # noqa: E501
        :rtype: AppSessionCompact
        """
        return self._parent_app_session

    @parent_app_session.setter
    def parent_app_session(self, parent_app_session):
        """Sets the parent_app_session of this V1pre3FileCompact.


        :param parent_app_session: The parent_app_session of this V1pre3FileCompact.  # noqa: E501
        :type: AppSessionCompact
        """

        self._parent_app_session = parent_app_session

    @property
    def parent_projects(self):
        """Gets the parent_projects of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_projects of this V1pre3FileCompact.  # noqa: E501
        :rtype: list[V1pre3ProjectCompact]
        """
        return self._parent_projects

    @parent_projects.setter
    def parent_projects(self, parent_projects):
        """Sets the parent_projects of this V1pre3FileCompact.


        :param parent_projects: The parent_projects of this V1pre3FileCompact.  # noqa: E501
        :type: list[V1pre3ProjectCompact]
        """

        self._parent_projects = parent_projects

    @property
    def category(self):
        """Gets the category of this V1pre3FileCompact.  # noqa: E501


        :return: The category of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this V1pre3FileCompact.


        :param category: The category of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def e_tag(self):
        """Gets the e_tag of this V1pre3FileCompact.  # noqa: E501


        :return: The e_tag of this V1pre3FileCompact.  # noqa: E501
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        """Sets the e_tag of this V1pre3FileCompact.


        :param e_tag: The e_tag of this V1pre3FileCompact.  # noqa: E501
        :type: str
        """

        self._e_tag = e_tag

    @property
    def parent_dataset(self):
        """Gets the parent_dataset of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_dataset of this V1pre3FileCompact.  # noqa: E501
        :rtype: V2DatasetCompact
        """
        return self._parent_dataset

    @parent_dataset.setter
    def parent_dataset(self, parent_dataset):
        """Sets the parent_dataset of this V1pre3FileCompact.


        :param parent_dataset: The parent_dataset of this V1pre3FileCompact.  # noqa: E501
        :type: V2DatasetCompact
        """

        self._parent_dataset = parent_dataset

    @property
    def parent_project(self):
        """Gets the parent_project of this V1pre3FileCompact.  # noqa: E501


        :return: The parent_project of this V1pre3FileCompact.  # noqa: E501
        :rtype: IProjectCompact
        """
        return self._parent_project

    @parent_project.setter
    def parent_project(self, parent_project):
        """Sets the parent_project of this V1pre3FileCompact.


        :param parent_project: The parent_project of this V1pre3FileCompact.  # noqa: E501
        :type: IProjectCompact
        """

        self._parent_project = parent_project

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
        if issubclass(V1pre3FileCompact, dict):
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
        if not isinstance(other, V1pre3FileCompact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1pre3FileCompact):
            return True

        return self.to_dict() != other.to_dict()
