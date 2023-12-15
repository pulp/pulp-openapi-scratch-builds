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

from pulpcore.client.pulpcore.configuration import Configuration


class AccessPolicyResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'permissions_assignment': 'list[object]',
        'creation_hooks': 'list[object]',
        'statements': 'list[object]',
        'viewset_name': 'str',
        'customized': 'bool',
        'queryset_scoping': 'object'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'permissions_assignment': 'permissions_assignment',
        'creation_hooks': 'creation_hooks',
        'statements': 'statements',
        'viewset_name': 'viewset_name',
        'customized': 'customized',
        'queryset_scoping': 'queryset_scoping'
    }

    def __init__(self, pulp_href=None, pulp_created=None, permissions_assignment=None, creation_hooks=None, statements=None, viewset_name=None, customized=None, queryset_scoping=None, local_vars_configuration=None):  # noqa: E501
        """AccessPolicyResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._permissions_assignment = None
        self._creation_hooks = None
        self._statements = None
        self._viewset_name = None
        self._customized = None
        self._queryset_scoping = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if permissions_assignment is not None:
            self.permissions_assignment = permissions_assignment
        if creation_hooks is not None:
            self.creation_hooks = creation_hooks
        self.statements = statements
        if viewset_name is not None:
            self.viewset_name = viewset_name
        if customized is not None:
            self.customized = customized
        if queryset_scoping is not None:
            self.queryset_scoping = queryset_scoping

    @property
    def pulp_href(self):
        """Gets the pulp_href of this AccessPolicyResponse.  # noqa: E501


        :return: The pulp_href of this AccessPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this AccessPolicyResponse.


        :param pulp_href: The pulp_href of this AccessPolicyResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this AccessPolicyResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this AccessPolicyResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this AccessPolicyResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this AccessPolicyResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def permissions_assignment(self):
        """Gets the permissions_assignment of this AccessPolicyResponse.  # noqa: E501

        List of callables that define the new permissions to be created for new objects.This is deprecated. Use `creation_hooks` instead.  # noqa: E501

        :return: The permissions_assignment of this AccessPolicyResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._permissions_assignment

    @permissions_assignment.setter
    def permissions_assignment(self, permissions_assignment):
        """Sets the permissions_assignment of this AccessPolicyResponse.

        List of callables that define the new permissions to be created for new objects.This is deprecated. Use `creation_hooks` instead.  # noqa: E501

        :param permissions_assignment: The permissions_assignment of this AccessPolicyResponse.  # noqa: E501
        :type: list[object]
        """

        self._permissions_assignment = permissions_assignment

    @property
    def creation_hooks(self):
        """Gets the creation_hooks of this AccessPolicyResponse.  # noqa: E501

        List of callables that may associate user roles for new objects.  # noqa: E501

        :return: The creation_hooks of this AccessPolicyResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._creation_hooks

    @creation_hooks.setter
    def creation_hooks(self, creation_hooks):
        """Sets the creation_hooks of this AccessPolicyResponse.

        List of callables that may associate user roles for new objects.  # noqa: E501

        :param creation_hooks: The creation_hooks of this AccessPolicyResponse.  # noqa: E501
        :type: list[object]
        """

        self._creation_hooks = creation_hooks

    @property
    def statements(self):
        """Gets the statements of this AccessPolicyResponse.  # noqa: E501

        List of policy statements defining the policy.  # noqa: E501

        :return: The statements of this AccessPolicyResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """Sets the statements of this AccessPolicyResponse.

        List of policy statements defining the policy.  # noqa: E501

        :param statements: The statements of this AccessPolicyResponse.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and statements is None:  # noqa: E501
            raise ValueError("Invalid value for `statements`, must not be `None`")  # noqa: E501

        self._statements = statements

    @property
    def viewset_name(self):
        """Gets the viewset_name of this AccessPolicyResponse.  # noqa: E501

        The name of ViewSet this AccessPolicy authorizes.  # noqa: E501

        :return: The viewset_name of this AccessPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._viewset_name

    @viewset_name.setter
    def viewset_name(self, viewset_name):
        """Sets the viewset_name of this AccessPolicyResponse.

        The name of ViewSet this AccessPolicy authorizes.  # noqa: E501

        :param viewset_name: The viewset_name of this AccessPolicyResponse.  # noqa: E501
        :type: str
        """

        self._viewset_name = viewset_name

    @property
    def customized(self):
        """Gets the customized of this AccessPolicyResponse.  # noqa: E501

        True if the AccessPolicy has been user-modified. False otherwise.  # noqa: E501

        :return: The customized of this AccessPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._customized

    @customized.setter
    def customized(self, customized):
        """Sets the customized of this AccessPolicyResponse.

        True if the AccessPolicy has been user-modified. False otherwise.  # noqa: E501

        :param customized: The customized of this AccessPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._customized = customized

    @property
    def queryset_scoping(self):
        """Gets the queryset_scoping of this AccessPolicyResponse.  # noqa: E501

        A callable for performing queryset scoping. See plugin documentation for valid callables. Set to blank to turn off queryset scoping.  # noqa: E501

        :return: The queryset_scoping of this AccessPolicyResponse.  # noqa: E501
        :rtype: object
        """
        return self._queryset_scoping

    @queryset_scoping.setter
    def queryset_scoping(self, queryset_scoping):
        """Sets the queryset_scoping of this AccessPolicyResponse.

        A callable for performing queryset scoping. See plugin documentation for valid callables. Set to blank to turn off queryset scoping.  # noqa: E501

        :param queryset_scoping: The queryset_scoping of this AccessPolicyResponse.  # noqa: E501
        :type: object
        """

        self._queryset_scoping = queryset_scoping

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
        if not isinstance(other, AccessPolicyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessPolicyResponse):
            return True

        return self.to_dict() != other.to_dict()
