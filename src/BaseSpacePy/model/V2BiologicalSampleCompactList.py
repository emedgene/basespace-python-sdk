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


class V2BiologicalSampleCompactList(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[V2BiologicalSampleCompact]',
        'paging': 'V2BiologicalSamplesSortFieldsV2Paging'
    }

    attribute_map = {
        'items': 'Items',
        'paging': 'Paging'
    }

    def __init__(self, items=None, paging=None, _configuration=None):  # noqa: E501
        """V2BiologicalSampleCompactList - a model defined for a BioSamples list representation"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._items = None
        self._paging = None
        self.discriminator = None

        self.items = items
        self.paging = paging

    @property
    def items(self):
        """Gets the items of this V2BiologicalSampleCompactList.  # noqa: E501


        :return: The items of this V2BiologicalSampleCompactList.  # noqa: E501
        :rtype: list[V2BiologicalSampleCompact]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this V2BiologicalSampleCompactList.


        :param items: The items of this V2BiologicalSampleCompactList.  # noqa: E501
        :type: list[V2BiologicalSampleCompact]
        """
        if self._configuration.client_side_validation and items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def paging(self):
        """Gets the paging of this V2BiologicalSampleCompactList.  # noqa: E501


        :return: The paging of this V2BiologicalSampleCompactList.  # noqa: E501
        :rtype: V2BiologicalSamplesSortFieldsV2Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this V2BiologicalSampleCompactList.


        :param paging: The paging of this V2BiologicalSampleCompactList.  # noqa: E501
        :type: V2BiologicalSamplesSortFieldsV2Paging
        """
        if self._configuration.client_side_validation and paging is None:
            raise ValueError("Invalid value for `paging`, must not be `None`")  # noqa: E501

        self._paging = paging

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
        if issubclass(V2BiologicalSampleCompactList, dict):
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
        if not isinstance(other, V2BiologicalSampleCompactList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2BiologicalSampleCompactList):
            return True

        return self.to_dict() != other.to_dict()
