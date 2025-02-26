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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from pulpcore.client.pulp_rpm.models.policy_enum import PolicyEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedrpmRpmRemote(BaseModel):
    """
    A Serializer for RpmRemote.
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A unique name for this remote.")
    url: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The URL of an external content source.")
    ca_cert: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A PEM encoded CA certificate used to validate the server certificate presented by the remote server.")
    client_cert: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A PEM encoded client certificate used for authentication.")
    client_key: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A PEM encoded private key used for authentication.")
    tls_validation: Optional[StrictBool] = Field(default=None, description="If True, TLS peer validation must be performed.")
    proxy_url: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The proxy URL. Format: scheme://host:port")
    proxy_username: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The username to authenticte to the proxy.")
    proxy_password: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The password to authenticate to the proxy. Extra leading and trailing whitespace characters are not trimmed.")
    username: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The username to be used for authentication when syncing.")
    password: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The password to be used for authentication when syncing. Extra leading and trailing whitespace characters are not trimmed.")
    pulp_labels: Optional[Dict[str, Optional[StrictStr]]] = None
    download_concurrency: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Total number of simultaneous connections. If not set then the default value will be used.")
    max_retries: Optional[StrictInt] = Field(default=None, description="Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used.")
    policy: Optional[PolicyEnum] = Field(default=None, description="The policy to use when downloading content. The possible values include: 'immediate', 'on_demand', and 'streamed'. 'immediate' is the default.  * `immediate` - When syncing, download all metadata and content now. * `on_demand` - When syncing, download metadata, but do not download content now. Instead, download content as clients request it, and save it in Pulp to be served for future client requests. * `streamed` - When syncing, download metadata, but do not download content now. Instead,download content as clients request it, but never save it in Pulp. This causes future requests for that same content to have to be downloaded again.")
    total_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    connect_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    sock_connect_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    sock_read_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    headers: Optional[List[Dict[str, Any]]] = Field(default=None, description="Headers for aiohttp.Clientsession")
    rate_limit: Optional[StrictInt] = Field(default=None, description="Limits requests per second for each concurrent downloader")
    sles_auth_token: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Authentication token for SLES repositories.")
    __properties: ClassVar[List[str]] = ["name", "url", "ca_cert", "client_cert", "client_key", "tls_validation", "proxy_url", "proxy_username", "proxy_password", "username", "password", "pulp_labels", "download_concurrency", "max_retries", "policy", "total_timeout", "connect_timeout", "sock_connect_timeout", "sock_read_timeout", "headers", "rate_limit", "sles_auth_token"]

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
        """Create an instance of PatchedrpmRpmRemote from a JSON string"""
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
        # set to None if ca_cert (nullable) is None
        # and model_fields_set contains the field
        if self.ca_cert is None and "ca_cert" in self.model_fields_set:
            _dict['ca_cert'] = None

        # set to None if client_cert (nullable) is None
        # and model_fields_set contains the field
        if self.client_cert is None and "client_cert" in self.model_fields_set:
            _dict['client_cert'] = None

        # set to None if client_key (nullable) is None
        # and model_fields_set contains the field
        if self.client_key is None and "client_key" in self.model_fields_set:
            _dict['client_key'] = None

        # set to None if proxy_url (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_url is None and "proxy_url" in self.model_fields_set:
            _dict['proxy_url'] = None

        # set to None if proxy_username (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_username is None and "proxy_username" in self.model_fields_set:
            _dict['proxy_username'] = None

        # set to None if proxy_password (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_password is None and "proxy_password" in self.model_fields_set:
            _dict['proxy_password'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if download_concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.download_concurrency is None and "download_concurrency" in self.model_fields_set:
            _dict['download_concurrency'] = None

        # set to None if max_retries (nullable) is None
        # and model_fields_set contains the field
        if self.max_retries is None and "max_retries" in self.model_fields_set:
            _dict['max_retries'] = None

        # set to None if total_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.total_timeout is None and "total_timeout" in self.model_fields_set:
            _dict['total_timeout'] = None

        # set to None if connect_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.connect_timeout is None and "connect_timeout" in self.model_fields_set:
            _dict['connect_timeout'] = None

        # set to None if sock_connect_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.sock_connect_timeout is None and "sock_connect_timeout" in self.model_fields_set:
            _dict['sock_connect_timeout'] = None

        # set to None if sock_read_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.sock_read_timeout is None and "sock_read_timeout" in self.model_fields_set:
            _dict['sock_read_timeout'] = None

        # set to None if rate_limit (nullable) is None
        # and model_fields_set contains the field
        if self.rate_limit is None and "rate_limit" in self.model_fields_set:
            _dict['rate_limit'] = None

        # set to None if sles_auth_token (nullable) is None
        # and model_fields_set contains the field
        if self.sles_auth_token is None and "sles_auth_token" in self.model_fields_set:
            _dict['sles_auth_token'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedrpmRpmRemote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "url": obj.get("url"),
            "ca_cert": obj.get("ca_cert"),
            "client_cert": obj.get("client_cert"),
            "client_key": obj.get("client_key"),
            "tls_validation": obj.get("tls_validation"),
            "proxy_url": obj.get("proxy_url"),
            "proxy_username": obj.get("proxy_username"),
            "proxy_password": obj.get("proxy_password"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "pulp_labels": obj.get("pulp_labels"),
            "download_concurrency": obj.get("download_concurrency"),
            "max_retries": obj.get("max_retries"),
            "policy": obj.get("policy"),
            "total_timeout": obj.get("total_timeout"),
            "connect_timeout": obj.get("connect_timeout"),
            "sock_connect_timeout": obj.get("sock_connect_timeout"),
            "sock_read_timeout": obj.get("sock_read_timeout"),
            "headers": obj.get("headers"),
            "rate_limit": obj.get("rate_limit"),
            "sles_auth_token": obj.get("sles_auth_token")
        })
        return _obj


