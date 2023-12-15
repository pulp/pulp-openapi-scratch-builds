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

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmRpmRepository(object):
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
        'pulp_labels': 'dict(str, str)',
        'name': 'str',
        'description': 'str',
        'retain_repo_versions': 'int',
        'remote': 'str',
        'autopublish': 'bool',
        'metadata_signing_service': 'str',
        'retain_package_versions': 'int',
        'metadata_checksum_type': 'MetadataChecksumTypeEnum',
        'package_checksum_type': 'PackageChecksumTypeEnum',
        'gpgcheck': 'int',
        'repo_gpgcheck': 'int',
        'sqlite_metadata': 'bool',
        'repo_config': 'object'
    }

    attribute_map = {
        'pulp_labels': 'pulp_labels',
        'name': 'name',
        'description': 'description',
        'retain_repo_versions': 'retain_repo_versions',
        'remote': 'remote',
        'autopublish': 'autopublish',
        'metadata_signing_service': 'metadata_signing_service',
        'retain_package_versions': 'retain_package_versions',
        'metadata_checksum_type': 'metadata_checksum_type',
        'package_checksum_type': 'package_checksum_type',
        'gpgcheck': 'gpgcheck',
        'repo_gpgcheck': 'repo_gpgcheck',
        'sqlite_metadata': 'sqlite_metadata',
        'repo_config': 'repo_config'
    }

    def __init__(self, pulp_labels=None, name=None, description=None, retain_repo_versions=None, remote=None, autopublish=False, metadata_signing_service=None, retain_package_versions=None, metadata_checksum_type=None, package_checksum_type=None, gpgcheck=None, repo_gpgcheck=None, sqlite_metadata=False, repo_config=None, local_vars_configuration=None):  # noqa: E501
        """RpmRpmRepository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_labels = None
        self._name = None
        self._description = None
        self._retain_repo_versions = None
        self._remote = None
        self._autopublish = None
        self._metadata_signing_service = None
        self._retain_package_versions = None
        self._metadata_checksum_type = None
        self._package_checksum_type = None
        self._gpgcheck = None
        self._repo_gpgcheck = None
        self._sqlite_metadata = None
        self._repo_config = None
        self.discriminator = None

        if pulp_labels is not None:
            self.pulp_labels = pulp_labels
        self.name = name
        self.description = description
        self.retain_repo_versions = retain_repo_versions
        self.remote = remote
        if autopublish is not None:
            self.autopublish = autopublish
        self.metadata_signing_service = metadata_signing_service
        if retain_package_versions is not None:
            self.retain_package_versions = retain_package_versions
        self.metadata_checksum_type = metadata_checksum_type
        self.package_checksum_type = package_checksum_type
        self.gpgcheck = gpgcheck
        self.repo_gpgcheck = repo_gpgcheck
        if sqlite_metadata is not None:
            self.sqlite_metadata = sqlite_metadata
        if repo_config is not None:
            self.repo_config = repo_config

    @property
    def pulp_labels(self):
        """Gets the pulp_labels of this RpmRpmRepository.  # noqa: E501


        :return: The pulp_labels of this RpmRpmRepository.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._pulp_labels

    @pulp_labels.setter
    def pulp_labels(self, pulp_labels):
        """Sets the pulp_labels of this RpmRpmRepository.


        :param pulp_labels: The pulp_labels of this RpmRpmRepository.  # noqa: E501
        :type: dict(str, str)
        """

        self._pulp_labels = pulp_labels

    @property
    def name(self):
        """Gets the name of this RpmRpmRepository.  # noqa: E501

        A unique name for this repository.  # noqa: E501

        :return: The name of this RpmRpmRepository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RpmRpmRepository.

        A unique name for this repository.  # noqa: E501

        :param name: The name of this RpmRpmRepository.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this RpmRpmRepository.  # noqa: E501

        An optional description.  # noqa: E501

        :return: The description of this RpmRpmRepository.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RpmRpmRepository.

        An optional description.  # noqa: E501

        :param description: The description of this RpmRpmRepository.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def retain_repo_versions(self):
        """Gets the retain_repo_versions of this RpmRpmRepository.  # noqa: E501

        Retain X versions of the repository. Default is null which retains all versions.  # noqa: E501

        :return: The retain_repo_versions of this RpmRpmRepository.  # noqa: E501
        :rtype: int
        """
        return self._retain_repo_versions

    @retain_repo_versions.setter
    def retain_repo_versions(self, retain_repo_versions):
        """Sets the retain_repo_versions of this RpmRpmRepository.

        Retain X versions of the repository. Default is null which retains all versions.  # noqa: E501

        :param retain_repo_versions: The retain_repo_versions of this RpmRpmRepository.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                retain_repo_versions is not None and retain_repo_versions < 1):  # noqa: E501
            raise ValueError("Invalid value for `retain_repo_versions`, must be a value greater than or equal to `1`")  # noqa: E501

        self._retain_repo_versions = retain_repo_versions

    @property
    def remote(self):
        """Gets the remote of this RpmRpmRepository.  # noqa: E501

        An optional remote to use by default when syncing.  # noqa: E501

        :return: The remote of this RpmRpmRepository.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this RpmRpmRepository.

        An optional remote to use by default when syncing.  # noqa: E501

        :param remote: The remote of this RpmRpmRepository.  # noqa: E501
        :type: str
        """

        self._remote = remote

    @property
    def autopublish(self):
        """Gets the autopublish of this RpmRpmRepository.  # noqa: E501

        Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository.  # noqa: E501

        :return: The autopublish of this RpmRpmRepository.  # noqa: E501
        :rtype: bool
        """
        return self._autopublish

    @autopublish.setter
    def autopublish(self, autopublish):
        """Sets the autopublish of this RpmRpmRepository.

        Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository.  # noqa: E501

        :param autopublish: The autopublish of this RpmRpmRepository.  # noqa: E501
        :type: bool
        """

        self._autopublish = autopublish

    @property
    def metadata_signing_service(self):
        """Gets the metadata_signing_service of this RpmRpmRepository.  # noqa: E501

        A reference to an associated signing service.  # noqa: E501

        :return: The metadata_signing_service of this RpmRpmRepository.  # noqa: E501
        :rtype: str
        """
        return self._metadata_signing_service

    @metadata_signing_service.setter
    def metadata_signing_service(self, metadata_signing_service):
        """Sets the metadata_signing_service of this RpmRpmRepository.

        A reference to an associated signing service.  # noqa: E501

        :param metadata_signing_service: The metadata_signing_service of this RpmRpmRepository.  # noqa: E501
        :type: str
        """

        self._metadata_signing_service = metadata_signing_service

    @property
    def retain_package_versions(self):
        """Gets the retain_package_versions of this RpmRpmRepository.  # noqa: E501

        The number of versions of each package to keep in the repository; older versions will be purged. The default is '0', which will disable this feature and keep all versions of each package.  # noqa: E501

        :return: The retain_package_versions of this RpmRpmRepository.  # noqa: E501
        :rtype: int
        """
        return self._retain_package_versions

    @retain_package_versions.setter
    def retain_package_versions(self, retain_package_versions):
        """Sets the retain_package_versions of this RpmRpmRepository.

        The number of versions of each package to keep in the repository; older versions will be purged. The default is '0', which will disable this feature and keep all versions of each package.  # noqa: E501

        :param retain_package_versions: The retain_package_versions of this RpmRpmRepository.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                retain_package_versions is not None and retain_package_versions < 0):  # noqa: E501
            raise ValueError("Invalid value for `retain_package_versions`, must be a value greater than or equal to `0`")  # noqa: E501

        self._retain_package_versions = retain_package_versions

    @property
    def metadata_checksum_type(self):
        """Gets the metadata_checksum_type of this RpmRpmRepository.  # noqa: E501

        The checksum type for metadata.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :return: The metadata_checksum_type of this RpmRpmRepository.  # noqa: E501
        :rtype: MetadataChecksumTypeEnum
        """
        return self._metadata_checksum_type

    @metadata_checksum_type.setter
    def metadata_checksum_type(self, metadata_checksum_type):
        """Sets the metadata_checksum_type of this RpmRpmRepository.

        The checksum type for metadata.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :param metadata_checksum_type: The metadata_checksum_type of this RpmRpmRepository.  # noqa: E501
        :type: MetadataChecksumTypeEnum
        """

        self._metadata_checksum_type = metadata_checksum_type

    @property
    def package_checksum_type(self):
        """Gets the package_checksum_type of this RpmRpmRepository.  # noqa: E501

        The checksum type for packages.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :return: The package_checksum_type of this RpmRpmRepository.  # noqa: E501
        :rtype: PackageChecksumTypeEnum
        """
        return self._package_checksum_type

    @package_checksum_type.setter
    def package_checksum_type(self, package_checksum_type):
        """Sets the package_checksum_type of this RpmRpmRepository.

        The checksum type for packages.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :param package_checksum_type: The package_checksum_type of this RpmRpmRepository.  # noqa: E501
        :type: PackageChecksumTypeEnum
        """

        self._package_checksum_type = package_checksum_type

    @property
    def gpgcheck(self):
        """Gets the gpgcheck of this RpmRpmRepository.  # noqa: E501

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages.  # noqa: E501

        :return: The gpgcheck of this RpmRpmRepository.  # noqa: E501
        :rtype: int
        """
        return self._gpgcheck

    @gpgcheck.setter
    def gpgcheck(self, gpgcheck):
        """Sets the gpgcheck of this RpmRpmRepository.

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages.  # noqa: E501

        :param gpgcheck: The gpgcheck of this RpmRpmRepository.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gpgcheck is not None and gpgcheck > 1):  # noqa: E501
            raise ValueError("Invalid value for `gpgcheck`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                gpgcheck is not None and gpgcheck < 0):  # noqa: E501
            raise ValueError("Invalid value for `gpgcheck`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gpgcheck = gpgcheck

    @property
    def repo_gpgcheck(self):
        """Gets the repo_gpgcheck of this RpmRpmRepository.  # noqa: E501

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata.  # noqa: E501

        :return: The repo_gpgcheck of this RpmRpmRepository.  # noqa: E501
        :rtype: int
        """
        return self._repo_gpgcheck

    @repo_gpgcheck.setter
    def repo_gpgcheck(self, repo_gpgcheck):
        """Sets the repo_gpgcheck of this RpmRpmRepository.

        DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata.  # noqa: E501

        :param repo_gpgcheck: The repo_gpgcheck of this RpmRpmRepository.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                repo_gpgcheck is not None and repo_gpgcheck > 1):  # noqa: E501
            raise ValueError("Invalid value for `repo_gpgcheck`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                repo_gpgcheck is not None and repo_gpgcheck < 0):  # noqa: E501
            raise ValueError("Invalid value for `repo_gpgcheck`, must be a value greater than or equal to `0`")  # noqa: E501

        self._repo_gpgcheck = repo_gpgcheck

    @property
    def sqlite_metadata(self):
        """Gets the sqlite_metadata of this RpmRpmRepository.  # noqa: E501

        DEPRECATED: An option specifying whether Pulp should generate SQLite metadata.  # noqa: E501

        :return: The sqlite_metadata of this RpmRpmRepository.  # noqa: E501
        :rtype: bool
        """
        return self._sqlite_metadata

    @sqlite_metadata.setter
    def sqlite_metadata(self, sqlite_metadata):
        """Sets the sqlite_metadata of this RpmRpmRepository.

        DEPRECATED: An option specifying whether Pulp should generate SQLite metadata.  # noqa: E501

        :param sqlite_metadata: The sqlite_metadata of this RpmRpmRepository.  # noqa: E501
        :type: bool
        """

        self._sqlite_metadata = sqlite_metadata

    @property
    def repo_config(self):
        """Gets the repo_config of this RpmRpmRepository.  # noqa: E501

        A JSON document describing config.repo file  # noqa: E501

        :return: The repo_config of this RpmRpmRepository.  # noqa: E501
        :rtype: object
        """
        return self._repo_config

    @repo_config.setter
    def repo_config(self, repo_config):
        """Sets the repo_config of this RpmRpmRepository.

        A JSON document describing config.repo file  # noqa: E501

        :param repo_config: The repo_config of this RpmRpmRepository.  # noqa: E501
        :type: object
        """

        self._repo_config = repo_config

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
        if not isinstance(other, RpmRpmRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmRpmRepository):
            return True

        return self.to_dict() != other.to_dict()
