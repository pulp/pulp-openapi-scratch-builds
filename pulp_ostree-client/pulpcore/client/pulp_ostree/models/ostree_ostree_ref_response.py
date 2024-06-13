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

from pulpcore.client.pulp_ostree.configuration import Configuration


class OstreeOstreeRefResponse(object):
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
        'pulp_last_updated': 'datetime',
        'artifact': 'str',
        'relative_path': 'str',
        'commit': 'str',
        'checksum': 'str',
        'name': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'artifact': 'artifact',
        'relative_path': 'relative_path',
        'commit': 'commit',
        'checksum': 'checksum',
        'name': 'name'
    }

    def __init__(self, pulp_href=None, pulp_created=None, pulp_last_updated=None, artifact=None, relative_path=None, commit=None, checksum=None, name=None, local_vars_configuration=None):  # noqa: E501
        """OstreeOstreeRefResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._artifact = None
        self._relative_path = None
        self._commit = None
        self._checksum = None
        self._name = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        self.artifact = artifact
        self.relative_path = relative_path
        self.commit = commit
        if checksum is not None:
            self.checksum = checksum
        self.name = name

    @property
    def pulp_href(self):
        """Gets the pulp_href of this OstreeOstreeRefResponse.  # noqa: E501


        :return: The pulp_href of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this OstreeOstreeRefResponse.


        :param pulp_href: The pulp_href of this OstreeOstreeRefResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this OstreeOstreeRefResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this OstreeOstreeRefResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this OstreeOstreeRefResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this OstreeOstreeRefResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this OstreeOstreeRefResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this OstreeOstreeRefResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def artifact(self):
        """Gets the artifact of this OstreeOstreeRefResponse.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this OstreeOstreeRefResponse.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this OstreeOstreeRefResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifact is None:  # noqa: E501
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this OstreeOstreeRefResponse.  # noqa: E501

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :return: The relative_path of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this OstreeOstreeRefResponse.

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :param relative_path: The relative_path of this OstreeOstreeRefResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relative_path is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def commit(self):
        """Gets the commit of this OstreeOstreeRefResponse.  # noqa: E501


        :return: The commit of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this OstreeOstreeRefResponse.


        :param commit: The commit of this OstreeOstreeRefResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and commit is None:  # noqa: E501
            raise ValueError("Invalid value for `commit`, must not be `None`")  # noqa: E501

        self._commit = commit

    @property
    def checksum(self):
        """Gets the checksum of this OstreeOstreeRefResponse.  # noqa: E501


        :return: The checksum of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this OstreeOstreeRefResponse.


        :param checksum: The checksum of this OstreeOstreeRefResponse.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def name(self):
        """Gets the name of this OstreeOstreeRefResponse.  # noqa: E501


        :return: The name of this OstreeOstreeRefResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OstreeOstreeRefResponse.


        :param name: The name of this OstreeOstreeRefResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, OstreeOstreeRefResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OstreeOstreeRefResponse):
            return True

        return self.to_dict() != other.to_dict()
