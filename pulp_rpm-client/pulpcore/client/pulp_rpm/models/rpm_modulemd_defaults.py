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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class RpmModulemdDefaults(BaseModel):
    """
    ModulemdDefaults serializer.
    """ # noqa: E501
    repository: Optional[StrictStr] = Field(default=None, description="A URI of a repository the new content unit should be associated with.")
    module: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Modulemd name.")
    stream: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Modulemd default stream.")
    profiles: Optional[Any] = Field(description="Default profiles for modulemd streams.")
    snippet: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Modulemd default snippet")
    __properties: ClassVar[List[str]] = ["repository", "module", "stream", "profiles", "snippet"]

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
        """Create an instance of RpmModulemdDefaults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if profiles (nullable) is None
        # and model_fields_set contains the field
        if self.profiles is None and "profiles" in self.model_fields_set:
            _dict['profiles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RpmModulemdDefaults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "repository": obj.get("repository"),
            "module": obj.get("module"),
            "stream": obj.get("stream"),
            "profiles": obj.get("profiles"),
            "snippet": obj.get("snippet")
        })
        return _obj


