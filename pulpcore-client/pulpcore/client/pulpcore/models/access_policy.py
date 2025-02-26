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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AccessPolicy(BaseModel):
    """
    Serializer for AccessPolicy.
    """ # noqa: E501
    permissions_assignment: Optional[List[Dict[str, Any]]] = Field(default=None, description="List of callables that define the new permissions to be created for new objects.This is deprecated. Use `creation_hooks` instead.")
    creation_hooks: Optional[List[Dict[str, Any]]] = Field(default=None, description="List of callables that may associate user roles for new objects.")
    statements: List[Dict[str, Any]] = Field(description="List of policy statements defining the policy.")
    queryset_scoping: Optional[Dict[str, Any]] = Field(default=None, description="A callable for performing queryset scoping. See plugin documentation for valid callables. Set to blank to turn off queryset scoping.")
    __properties: ClassVar[List[str]] = ["permissions_assignment", "creation_hooks", "statements", "queryset_scoping"]

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
        """Create an instance of AccessPolicy from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "permissions_assignment": obj.get("permissions_assignment"),
            "creation_hooks": obj.get("creation_hooks"),
            "statements": obj.get("statements"),
            "queryset_scoping": obj.get("queryset_scoping")
        })
        return _obj


