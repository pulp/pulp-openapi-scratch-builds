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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RpmPackageEnvironmentResponse(BaseModel):
    """
    PackageEnvironment serializer.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    pulp_created: Optional[datetime] = Field(default=None, description="Timestamp of creation.")
    pulp_last_updated: Optional[datetime] = Field(default=None, description="Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.")
    id: StrictStr = Field(description="Environment id.")
    name: StrictStr = Field(description="Environment name.")
    description: StrictStr = Field(description="Environment description.")
    display_order: Optional[StrictInt] = Field(description="Environment display order.")
    group_ids: Optional[Any] = Field(description="Environment group list.")
    option_ids: Optional[Any] = Field(description="Environment option ids")
    desc_by_lang: Optional[Any] = Field(description="Environment description by language.")
    name_by_lang: Optional[Any] = Field(description="Environment name by language.")
    digest: StrictStr = Field(description="Environment digest.")
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "pulp_created", "pulp_last_updated", "id", "name", "description", "display_order", "group_ids", "option_ids", "desc_by_lang", "name_by_lang", "digest"]

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
        """Create an instance of RpmPackageEnvironmentResponse from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "pulp_href",
            "prn",
            "pulp_created",
            "pulp_last_updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if display_order (nullable) is None
        # and model_fields_set contains the field
        if self.display_order is None and "display_order" in self.model_fields_set:
            _dict['display_order'] = None

        # set to None if group_ids (nullable) is None
        # and model_fields_set contains the field
        if self.group_ids is None and "group_ids" in self.model_fields_set:
            _dict['group_ids'] = None

        # set to None if option_ids (nullable) is None
        # and model_fields_set contains the field
        if self.option_ids is None and "option_ids" in self.model_fields_set:
            _dict['option_ids'] = None

        # set to None if desc_by_lang (nullable) is None
        # and model_fields_set contains the field
        if self.desc_by_lang is None and "desc_by_lang" in self.model_fields_set:
            _dict['desc_by_lang'] = None

        # set to None if name_by_lang (nullable) is None
        # and model_fields_set contains the field
        if self.name_by_lang is None and "name_by_lang" in self.model_fields_set:
            _dict['name_by_lang'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RpmPackageEnvironmentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "pulp_created": obj.get("pulp_created"),
            "pulp_last_updated": obj.get("pulp_last_updated"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "display_order": obj.get("display_order"),
            "group_ids": obj.get("group_ids"),
            "option_ids": obj.get("option_ids"),
            "desc_by_lang": obj.get("desc_by_lang"),
            "name_by_lang": obj.get("name_by_lang"),
            "digest": obj.get("digest")
        })
        return _obj


