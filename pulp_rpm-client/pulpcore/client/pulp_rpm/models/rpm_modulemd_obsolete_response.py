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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RpmModulemdObsoleteResponse(BaseModel):
    """
    ModulemdObsolete serializer.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    pulp_created: Optional[datetime] = Field(default=None, description="Timestamp of creation.")
    pulp_last_updated: Optional[datetime] = Field(default=None, description="Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.")
    modified: StrictStr = Field(description="Obsolete modified time.")
    module_name: StrictStr = Field(description="Modulemd name.")
    module_stream: StrictStr = Field(description="Modulemd's stream.")
    message: StrictStr = Field(description="Obsolete description.")
    override_previous: Optional[StrictStr] = Field(description="Reset previous obsoletes.")
    module_context: Optional[StrictStr] = Field(description="Modulemd's context.")
    eol_date: Optional[StrictStr] = Field(description="End of Life date.")
    obsoleted_by_module_name: Optional[StrictStr] = Field(description="Obsolete by module name.")
    obsoleted_by_module_stream: Optional[StrictStr] = Field(description="Obsolete by module stream.")
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "pulp_created", "pulp_last_updated", "modified", "module_name", "module_stream", "message", "override_previous", "module_context", "eol_date", "obsoleted_by_module_name", "obsoleted_by_module_stream"]

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
        """Create an instance of RpmModulemdObsoleteResponse from a JSON string"""
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
        # set to None if override_previous (nullable) is None
        # and model_fields_set contains the field
        if self.override_previous is None and "override_previous" in self.model_fields_set:
            _dict['override_previous'] = None

        # set to None if module_context (nullable) is None
        # and model_fields_set contains the field
        if self.module_context is None and "module_context" in self.model_fields_set:
            _dict['module_context'] = None

        # set to None if eol_date (nullable) is None
        # and model_fields_set contains the field
        if self.eol_date is None and "eol_date" in self.model_fields_set:
            _dict['eol_date'] = None

        # set to None if obsoleted_by_module_name (nullable) is None
        # and model_fields_set contains the field
        if self.obsoleted_by_module_name is None and "obsoleted_by_module_name" in self.model_fields_set:
            _dict['obsoleted_by_module_name'] = None

        # set to None if obsoleted_by_module_stream (nullable) is None
        # and model_fields_set contains the field
        if self.obsoleted_by_module_stream is None and "obsoleted_by_module_stream" in self.model_fields_set:
            _dict['obsoleted_by_module_stream'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RpmModulemdObsoleteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "pulp_created": obj.get("pulp_created"),
            "pulp_last_updated": obj.get("pulp_last_updated"),
            "modified": obj.get("modified"),
            "module_name": obj.get("module_name"),
            "module_stream": obj.get("module_stream"),
            "message": obj.get("message"),
            "override_previous": obj.get("override_previous"),
            "module_context": obj.get("module_context"),
            "eol_date": obj.get("eol_date"),
            "obsoleted_by_module_name": obj.get("obsoleted_by_module_name"),
            "obsoleted_by_module_stream": obj.get("obsoleted_by_module_stream")
        })
        return _obj


