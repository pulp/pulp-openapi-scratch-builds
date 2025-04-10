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

class PulpExport(BaseModel):
    """
    Serializer for PulpExports.
    """ # noqa: E501
    task: Optional[StrictStr] = Field(default=None, description="A URI of the task that ran the Export.")
    full: Optional[StrictBool] = Field(default=True, description="Do a Full (true) or Incremental (false) export.")
    dry_run: Optional[StrictBool] = Field(default=False, description="Generate report on what would be exported and disk-space required.")
    versions: Optional[List[StrictStr]] = Field(default=None, description="List of explicit repo-version hrefs to export (replaces current_version).")
    chunk_size: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Chunk export-tarfile into pieces of chunk_size bytes. Recognizes units of B/KB/MB/GB/TB. A chunk has a maximum size of 1TB.")
    start_versions: Optional[List[StrictStr]] = Field(default=None, description="List of explicit last-exported-repo-version hrefs (replaces last_export).")
    __properties: ClassVar[List[str]] = ["task", "full", "dry_run", "versions", "chunk_size", "start_versions"]

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
        """Create an instance of PulpExport from a JSON string"""
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
        # set to None if task (nullable) is None
        # and model_fields_set contains the field
        if self.task is None and "task" in self.model_fields_set:
            _dict['task'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PulpExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task": obj.get("task"),
            "full": obj.get("full") if obj.get("full") is not None else True,
            "dry_run": obj.get("dry_run") if obj.get("dry_run") is not None else False,
            "versions": obj.get("versions"),
            "chunk_size": obj.get("chunk_size"),
            "start_versions": obj.get("start_versions")
        })
        return _obj


