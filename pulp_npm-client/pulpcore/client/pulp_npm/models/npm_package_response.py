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

from pulpcore.client.pulp_npm.configuration import Configuration


class NpmPackageResponse(object):
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
        'prn': 'str',
        'pulp_created': 'datetime',
        'pulp_last_updated': 'datetime',
        'artifact': 'str',
        'relative_path': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'prn': 'prn',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'artifact': 'artifact',
        'relative_path': 'relative_path',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, pulp_href=None, prn=None, pulp_created=None, pulp_last_updated=None, artifact=None, relative_path=None, name=None, version=None, local_vars_configuration=None):  # noqa: E501
        """NpmPackageResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._prn = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._artifact = None
        self._relative_path = None
        self._name = None
        self._version = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if prn is not None:
            self.prn = prn
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        if artifact is not None:
            self.artifact = artifact
        self.relative_path = relative_path
        self.name = name
        self.version = version

    @property
    def pulp_href(self):
        """Gets the pulp_href of this NpmPackageResponse.  # noqa: E501


        :return: The pulp_href of this NpmPackageResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this NpmPackageResponse.


        :param pulp_href: The pulp_href of this NpmPackageResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def prn(self):
        """Gets the prn of this NpmPackageResponse.  # noqa: E501

        The Pulp Resource Name (PRN).  # noqa: E501

        :return: The prn of this NpmPackageResponse.  # noqa: E501
        :rtype: str
        """
        return self._prn

    @prn.setter
    def prn(self, prn):
        """Sets the prn of this NpmPackageResponse.

        The Pulp Resource Name (PRN).  # noqa: E501

        :param prn: The prn of this NpmPackageResponse.  # noqa: E501
        :type: str
        """

        self._prn = prn

    @property
    def pulp_created(self):
        """Gets the pulp_created of this NpmPackageResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this NpmPackageResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this NpmPackageResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this NpmPackageResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this NpmPackageResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this NpmPackageResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this NpmPackageResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this NpmPackageResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def artifact(self):
        """Gets the artifact of this NpmPackageResponse.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this NpmPackageResponse.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this NpmPackageResponse.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this NpmPackageResponse.  # noqa: E501
        :type: str
        """

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this NpmPackageResponse.  # noqa: E501


        :return: The relative_path of this NpmPackageResponse.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this NpmPackageResponse.


        :param relative_path: The relative_path of this NpmPackageResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relative_path is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def name(self):
        """Gets the name of this NpmPackageResponse.  # noqa: E501


        :return: The name of this NpmPackageResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NpmPackageResponse.


        :param name: The name of this NpmPackageResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this NpmPackageResponse.  # noqa: E501


        :return: The version of this NpmPackageResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NpmPackageResponse.


        :param version: The version of this NpmPackageResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, NpmPackageResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NpmPackageResponse):
            return True

        return self.to_dict() != other.to_dict()
