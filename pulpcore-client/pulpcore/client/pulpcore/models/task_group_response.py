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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pulpcore.client.pulpcore.models.group_progress_report_response import GroupProgressReportResponse
from pulpcore.client.pulpcore.models.minimal_task_response import MinimalTaskResponse
from typing import Optional, Set
from typing_extensions import Self

class TaskGroupResponse(BaseModel):
    """
    Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    description: StrictStr = Field(description="A description of the task group.")
    all_tasks_dispatched: StrictBool = Field(description="Whether all tasks have been spawned for this task group.")
    waiting: Optional[StrictInt] = Field(default=None, description="Number of tasks in the 'waiting' state")
    skipped: Optional[StrictInt] = Field(default=None, description="Number of tasks in the 'skipped' state")
    running: Optional[StrictInt] = Field(default=None, description="Number of tasks in the 'running' state")
    completed: Optional[StrictInt] = Field(default=None, description="Number of tasks in the 'completed' state")
    canceled: Optional[StrictInt] = Field(default=None, description="Number of tasks in the 'canceled' state")
    failed: Optional[StrictInt] = Field(default=None, description="Number of tasks in the 'failed' state")
    canceling: Optional[StrictInt] = Field(default=None, description="Number of tasks in the 'canceling' state")
    group_progress_reports: Optional[List[GroupProgressReportResponse]] = None
    tasks: Optional[List[MinimalTaskResponse]] = None
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "description", "all_tasks_dispatched", "waiting", "skipped", "running", "completed", "canceled", "failed", "canceling", "group_progress_reports", "tasks"]

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
        """Create an instance of TaskGroupResponse from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pulp_href",
            "prn",
            "waiting",
            "skipped",
            "running",
            "completed",
            "canceled",
            "failed",
            "canceling",
            "group_progress_reports",
            "tasks",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in group_progress_reports (list)
        _items = []
        if self.group_progress_reports:
            for _item_group_progress_reports in self.group_progress_reports:
                if _item_group_progress_reports:
                    _items.append(_item_group_progress_reports.to_dict())
            _dict['group_progress_reports'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tasks (list)
        _items = []
        if self.tasks:
            for _item_tasks in self.tasks:
                if _item_tasks:
                    _items.append(_item_tasks.to_dict())
            _dict['tasks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TaskGroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "description": obj.get("description"),
            "all_tasks_dispatched": obj.get("all_tasks_dispatched"),
            "waiting": obj.get("waiting"),
            "skipped": obj.get("skipped"),
            "running": obj.get("running"),
            "completed": obj.get("completed"),
            "canceled": obj.get("canceled"),
            "failed": obj.get("failed"),
            "canceling": obj.get("canceling"),
            "group_progress_reports": [GroupProgressReportResponse.from_dict(_item) for _item in obj["group_progress_reports"]] if obj.get("group_progress_reports") is not None else None,
            "tasks": [MinimalTaskResponse.from_dict(_item) for _item in obj["tasks"]] if obj.get("tasks") is not None else None
        })
        return _obj


