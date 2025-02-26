# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pulpcore.client.pulp_rpm.models.compression_type_enum import CompressionTypeEnum
from pulpcore.client.pulp_rpm.models.package_checksum_type_enum import PackageChecksumTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class RpmRpmPublicationResponse(BaseModel):
    """
    A Serializer for RpmPublication.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    pulp_created: Optional[datetime] = Field(default=None, description="Timestamp of creation.")
    pulp_last_updated: Optional[datetime] = Field(default=None, description="Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.")
    repository_version: Optional[StrictStr] = None
    repository: Optional[StrictStr] = Field(default=None, description="A URI of the repository to be published.")
    checksum_type: Optional[PackageChecksumTypeEnum] = Field(default=None, description="The preferred checksum type used during repo publishes.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512")
    metadata_checksum_type: Optional[PackageChecksumTypeEnum] = Field(default=None, description="DEPRECATED: The checksum type for metadata.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512")
    package_checksum_type: Optional[PackageChecksumTypeEnum] = Field(default=None, description="DEPRECATED: The checksum type for packages.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512")
    gpgcheck: Optional[Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(default=None, description="DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages.")
    repo_gpgcheck: Optional[Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(default=None, description="DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata.")
    sqlite_metadata: Optional[StrictBool] = Field(default=False, description="REMOVED: An option specifying whether Pulp should generate SQLite metadata. Not operation since pulp_rpm 3.25.0 release")
    repo_config: Optional[Any] = Field(default=None, description="A JSON document describing config.repo file")
    compression_type: Optional[CompressionTypeEnum] = Field(default=None, description="The compression type to use for metadata files.  * `zstd` - zstd * `gz` - gz")
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "pulp_created", "pulp_last_updated", "repository_version", "repository", "checksum_type", "metadata_checksum_type", "package_checksum_type", "gpgcheck", "repo_gpgcheck", "sqlite_metadata", "repo_config", "compression_type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RpmRpmPublicationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pulp_href",
            "prn",
            "pulp_created",
            "pulp_last_updated",
            "sqlite_metadata",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if gpgcheck (nullable) is None
        # and model_fields_set contains the field
        if self.gpgcheck is None and "gpgcheck" in self.model_fields_set:
            _dict['gpgcheck'] = None

        # set to None if repo_gpgcheck (nullable) is None
        # and model_fields_set contains the field
        if self.repo_gpgcheck is None and "repo_gpgcheck" in self.model_fields_set:
            _dict['repo_gpgcheck'] = None

        # set to None if repo_config (nullable) is None
        # and model_fields_set contains the field
        if self.repo_config is None and "repo_config" in self.model_fields_set:
            _dict['repo_config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RpmRpmPublicationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "pulp_created": obj.get("pulp_created"),
            "pulp_last_updated": obj.get("pulp_last_updated"),
            "repository_version": obj.get("repository_version"),
            "repository": obj.get("repository"),
            "checksum_type": obj.get("checksum_type"),
            "metadata_checksum_type": obj.get("metadata_checksum_type"),
            "package_checksum_type": obj.get("package_checksum_type"),
            "gpgcheck": obj.get("gpgcheck"),
            "repo_gpgcheck": obj.get("repo_gpgcheck"),
            "sqlite_metadata": obj.get("sqlite_metadata") if obj.get("sqlite_metadata") is not None else False,
            "repo_config": obj.get("repo_config"),
            "compression_type": obj.get("compression_type")
        })
        return _obj


