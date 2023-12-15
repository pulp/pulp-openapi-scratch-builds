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


class NestedRoleResponse(object):
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
        'users': 'list[str]',
        'groups': 'list[str]',
        'role': 'str'
    }

    attribute_map = {
        'users': 'users',
        'groups': 'groups',
        'role': 'role'
    }

    def __init__(self, users=[], groups=[], role=None, local_vars_configuration=None):  # noqa: E501
        """NestedRoleResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._users = None
        self._groups = None
        self._role = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if groups is not None:
            self.groups = groups
        self.role = role

    @property
    def users(self):
        """Gets the users of this NestedRoleResponse.  # noqa: E501


        :return: The users of this NestedRoleResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this NestedRoleResponse.


        :param users: The users of this NestedRoleResponse.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def groups(self):
        """Gets the groups of this NestedRoleResponse.  # noqa: E501


        :return: The groups of this NestedRoleResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this NestedRoleResponse.


        :param groups: The groups of this NestedRoleResponse.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def role(self):
        """Gets the role of this NestedRoleResponse.  # noqa: E501


        :return: The role of this NestedRoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NestedRoleResponse.


        :param role: The role of this NestedRoleResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

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
        if not isinstance(other, NestedRoleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedRoleResponse):
            return True

        return self.to_dict() != other.to_dict()
