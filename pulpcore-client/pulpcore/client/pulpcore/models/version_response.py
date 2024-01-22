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


class VersionResponse(object):
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
        'component': 'str',
        'version': 'str',
        'package': 'str',
        'module': 'str',
        'domain_compatible': 'bool'
    }

    attribute_map = {
        'component': 'component',
        'version': 'version',
        'package': 'package',
        'module': 'module',
        'domain_compatible': 'domain_compatible'
    }

    def __init__(self, component=None, version=None, package=None, module=None, domain_compatible=None, local_vars_configuration=None):  # noqa: E501
        """VersionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._component = None
        self._version = None
        self._package = None
        self._module = None
        self._domain_compatible = None
        self.discriminator = None

        self.component = component
        self.version = version
        self.package = package
        self.module = module
        self.domain_compatible = domain_compatible

    @property
    def component(self):
        """Gets the component of this VersionResponse.  # noqa: E501

        Name of a versioned component of Pulp  # noqa: E501

        :return: The component of this VersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this VersionResponse.

        Name of a versioned component of Pulp  # noqa: E501

        :param component: The component of this VersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and component is None:  # noqa: E501
            raise ValueError("Invalid value for `component`, must not be `None`")  # noqa: E501

        self._component = component

    @property
    def version(self):
        """Gets the version of this VersionResponse.  # noqa: E501

        Version of the component (e.g. 3.0.0)  # noqa: E501

        :return: The version of this VersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionResponse.

        Version of the component (e.g. 3.0.0)  # noqa: E501

        :param version: The version of this VersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def package(self):
        """Gets the package of this VersionResponse.  # noqa: E501

        Python package name providing the component  # noqa: E501

        :return: The package of this VersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this VersionResponse.

        Python package name providing the component  # noqa: E501

        :param package: The package of this VersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and package is None:  # noqa: E501
            raise ValueError("Invalid value for `package`, must not be `None`")  # noqa: E501

        self._package = package

    @property
    def module(self):
        """Gets the module of this VersionResponse.  # noqa: E501

        Python module name of the component  # noqa: E501

        :return: The module of this VersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this VersionResponse.

        Python module name of the component  # noqa: E501

        :param module: The module of this VersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and module is None:  # noqa: E501
            raise ValueError("Invalid value for `module`, must not be `None`")  # noqa: E501

        self._module = module

    @property
    def domain_compatible(self):
        """Gets the domain_compatible of this VersionResponse.  # noqa: E501

        Domain feature compatibility of component  # noqa: E501

        :return: The domain_compatible of this VersionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._domain_compatible

    @domain_compatible.setter
    def domain_compatible(self, domain_compatible):
        """Sets the domain_compatible of this VersionResponse.

        Domain feature compatibility of component  # noqa: E501

        :param domain_compatible: The domain_compatible of this VersionResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and domain_compatible is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_compatible`, must not be `None`")  # noqa: E501

        self._domain_compatible = domain_compatible

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
        if not isinstance(other, VersionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VersionResponse):
            return True

        return self.to_dict() != other.to_dict()
