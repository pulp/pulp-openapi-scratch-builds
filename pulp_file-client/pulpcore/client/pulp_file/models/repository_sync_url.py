# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_file.configuration import Configuration


class RepositorySyncURL(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'remote': 'str',
        'mirror': 'bool'
    }

    attribute_map = {
        'remote': 'remote',
        'mirror': 'mirror'
    }

    def __init__(self, remote=None, mirror=False, local_vars_configuration=None):  # noqa: E501
        """RepositorySyncURL - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._remote = None
        self._mirror = None
        self.discriminator = None

        if remote is not None:
            self.remote = remote
        if mirror is not None:
            self.mirror = mirror

    @property
    def remote(self):
        """Gets the remote of this RepositorySyncURL.  # noqa: E501

        A remote to sync from. This will override a remote set on repository.  # noqa: E501

        :return: The remote of this RepositorySyncURL.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this RepositorySyncURL.

        A remote to sync from. This will override a remote set on repository.  # noqa: E501

        :param remote: The remote of this RepositorySyncURL.  # noqa: E501
        :type: str
        """

        self._remote = remote

    @property
    def mirror(self):
        """Gets the mirror of this RepositorySyncURL.  # noqa: E501

        If ``True``, synchronization will remove all content that is not present in the remote repository. If ``False``, sync will be additive only.  # noqa: E501

        :return: The mirror of this RepositorySyncURL.  # noqa: E501
        :rtype: bool
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this RepositorySyncURL.

        If ``True``, synchronization will remove all content that is not present in the remote repository. If ``False``, sync will be additive only.  # noqa: E501

        :param mirror: The mirror of this RepositorySyncURL.  # noqa: E501
        :type: bool
        """

        self._mirror = mirror

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepositorySyncURL):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositorySyncURL):
            return True

        return self.to_dict() != other.to_dict()
