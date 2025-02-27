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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PatchedmavenMavenDistribution(BaseModel):
    """
    Serializer for Maven Distributions.
    """ # noqa: E501
    base_path: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \"foo\" and \"foo/bar\")")
    content_guard: Optional[StrictStr] = Field(default=None, description="An optional content-guard.")
    hidden: Optional[StrictBool] = Field(default=False, description="Whether this distribution should be shown in the content app.")
    pulp_labels: Optional[Dict[str, Optional[StrictStr]]] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A unique name. Ex, `rawhide` and `stable`.")
    repository: Optional[StrictStr] = Field(default=None, description="The latest RepositoryVersion for this Repository will be served.")
    remote: Optional[StrictStr] = Field(default=None, description="Remote that can be used to fetch content when using pull-through caching.")
    __properties: ClassVar[List[str]] = ["base_path", "content_guard", "hidden", "pulp_labels", "name", "repository", "remote"]

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
        """Create an instance of PatchedmavenMavenDistribution from a JSON string"""
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
        # set to None if content_guard (nullable) is None
        # and model_fields_set contains the field
        if self.content_guard is None and "content_guard" in self.model_fields_set:
            _dict['content_guard'] = None

        # set to None if repository (nullable) is None
        # and model_fields_set contains the field
        if self.repository is None and "repository" in self.model_fields_set:
            _dict['repository'] = None

        # set to None if remote (nullable) is None
        # and model_fields_set contains the field
        if self.remote is None and "remote" in self.model_fields_set:
            _dict['remote'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedmavenMavenDistribution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "base_path": obj.get("base_path"),
            "content_guard": obj.get("content_guard"),
            "hidden": obj.get("hidden") if obj.get("hidden") is not None else False,
            "pulp_labels": obj.get("pulp_labels"),
            "name": obj.get("name"),
            "repository": obj.get("repository"),
            "remote": obj.get("remote")
        })
        return _obj


