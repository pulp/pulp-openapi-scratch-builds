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
from typing_extensions import Annotated
from pulpcore.client.pulpcore.models.nested_open_pgp_public_subkey_response import NestedOpenPGPPublicSubkeyResponse
from pulpcore.client.pulpcore.models.nested_open_pgp_user_attribute_response import NestedOpenPGPUserAttributeResponse
from pulpcore.client.pulpcore.models.nested_open_pgp_user_id_response import NestedOpenPGPUserIDResponse
from typing import Optional, Set
from typing_extensions import Self

class OpenPGPPublicKeyResponse(BaseModel):
    """
    A serializer for content types with no Artifact.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    pulp_created: Optional[datetime] = Field(default=None, description="Timestamp of creation.")
    pulp_last_updated: Optional[datetime] = Field(default=None, description="Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.")
    fingerprint: Optional[Annotated[str, Field(strict=True, max_length=64)]] = None
    created: Optional[datetime] = None
    user_ids: Optional[List[NestedOpenPGPUserIDResponse]] = None
    user_attributes: Optional[List[NestedOpenPGPUserAttributeResponse]] = None
    public_subkeys: Optional[List[NestedOpenPGPPublicSubkeyResponse]] = None
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "pulp_created", "pulp_last_updated", "fingerprint", "created", "user_ids", "user_attributes", "public_subkeys"]

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
        """Create an instance of OpenPGPPublicKeyResponse from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "pulp_href",
            "prn",
            "pulp_created",
            "pulp_last_updated",
            "fingerprint",
            "created",
            "user_ids",
            "user_attributes",
            "public_subkeys",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in user_ids (list)
        _items = []
        if self.user_ids:
            for _item_user_ids in self.user_ids:
                if _item_user_ids:
                    _items.append(_item_user_ids.to_dict())
            _dict['user_ids'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in user_attributes (list)
        _items = []
        if self.user_attributes:
            for _item_user_attributes in self.user_attributes:
                if _item_user_attributes:
                    _items.append(_item_user_attributes.to_dict())
            _dict['user_attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in public_subkeys (list)
        _items = []
        if self.public_subkeys:
            for _item_public_subkeys in self.public_subkeys:
                if _item_public_subkeys:
                    _items.append(_item_public_subkeys.to_dict())
            _dict['public_subkeys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenPGPPublicKeyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "pulp_created": obj.get("pulp_created"),
            "pulp_last_updated": obj.get("pulp_last_updated"),
            "fingerprint": obj.get("fingerprint"),
            "created": obj.get("created"),
            "user_ids": [NestedOpenPGPUserIDResponse.from_dict(_item) for _item in obj["user_ids"]] if obj.get("user_ids") is not None else None,
            "user_attributes": [NestedOpenPGPUserAttributeResponse.from_dict(_item) for _item in obj["user_attributes"]] if obj.get("user_attributes") is not None else None,
            "public_subkeys": [NestedOpenPGPPublicSubkeyResponse.from_dict(_item) for _item in obj["public_subkeys"]] if obj.get("public_subkeys") is not None else None
        })
        return _obj


