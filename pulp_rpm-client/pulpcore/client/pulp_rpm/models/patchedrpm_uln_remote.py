# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class PatchedrpmUlnRemote(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'url': 'str',
        'ca_cert': 'str',
        'client_cert': 'str',
        'client_key': 'str',
        'tls_validation': 'bool',
        'proxy_url': 'str',
        'proxy_username': 'str',
        'proxy_password': 'str',
        'username': 'str',
        'password': 'str',
        'pulp_labels': 'dict(str, str)',
        'download_concurrency': 'int',
        'max_retries': 'int',
        'policy': 'PolicyEnum',
        'total_timeout': 'float',
        'connect_timeout': 'float',
        'sock_connect_timeout': 'float',
        'sock_read_timeout': 'float',
        'headers': 'list[object]',
        'rate_limit': 'int',
        'uln_server_base_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'ca_cert': 'ca_cert',
        'client_cert': 'client_cert',
        'client_key': 'client_key',
        'tls_validation': 'tls_validation',
        'proxy_url': 'proxy_url',
        'proxy_username': 'proxy_username',
        'proxy_password': 'proxy_password',
        'username': 'username',
        'password': 'password',
        'pulp_labels': 'pulp_labels',
        'download_concurrency': 'download_concurrency',
        'max_retries': 'max_retries',
        'policy': 'policy',
        'total_timeout': 'total_timeout',
        'connect_timeout': 'connect_timeout',
        'sock_connect_timeout': 'sock_connect_timeout',
        'sock_read_timeout': 'sock_read_timeout',
        'headers': 'headers',
        'rate_limit': 'rate_limit',
        'uln_server_base_url': 'uln_server_base_url'
    }

    def __init__(self, name=None, url=None, ca_cert=None, client_cert=None, client_key=None, tls_validation=None, proxy_url=None, proxy_username=None, proxy_password=None, username=None, password=None, pulp_labels=None, download_concurrency=None, max_retries=None, policy=None, total_timeout=None, connect_timeout=None, sock_connect_timeout=None, sock_read_timeout=None, headers=None, rate_limit=None, uln_server_base_url=None, local_vars_configuration=None):  # noqa: E501
        """PatchedrpmUlnRemote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._url = None
        self._ca_cert = None
        self._client_cert = None
        self._client_key = None
        self._tls_validation = None
        self._proxy_url = None
        self._proxy_username = None
        self._proxy_password = None
        self._username = None
        self._password = None
        self._pulp_labels = None
        self._download_concurrency = None
        self._max_retries = None
        self._policy = None
        self._total_timeout = None
        self._connect_timeout = None
        self._sock_connect_timeout = None
        self._sock_read_timeout = None
        self._headers = None
        self._rate_limit = None
        self._uln_server_base_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        self.ca_cert = ca_cert
        self.client_cert = client_cert
        self.client_key = client_key
        if tls_validation is not None:
            self.tls_validation = tls_validation
        self.proxy_url = proxy_url
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if pulp_labels is not None:
            self.pulp_labels = pulp_labels
        self.download_concurrency = download_concurrency
        self.max_retries = max_retries
        if policy is not None:
            self.policy = policy
        self.total_timeout = total_timeout
        self.connect_timeout = connect_timeout
        self.sock_connect_timeout = sock_connect_timeout
        self.sock_read_timeout = sock_read_timeout
        if headers is not None:
            self.headers = headers
        self.rate_limit = rate_limit
        self.uln_server_base_url = uln_server_base_url

    @property
    def name(self):
        """Gets the name of this PatchedrpmUlnRemote.  # noqa: E501

        A unique name for this remote.  # noqa: E501

        :return: The name of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedrpmUlnRemote.

        A unique name for this remote.  # noqa: E501

        :param name: The name of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this PatchedrpmUlnRemote.  # noqa: E501

        The ULN repo URL of the remote content source.\"This is \"uln://\" followed by the channel name. E.g.: \"uln://ol7_x86_64_oracle\"  # noqa: E501

        :return: The url of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PatchedrpmUlnRemote.

        The ULN repo URL of the remote content source.\"This is \"uln://\" followed by the channel name. E.g.: \"uln://ol7_x86_64_oracle\"  # noqa: E501

        :param url: The url of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def ca_cert(self):
        """Gets the ca_cert of this PatchedrpmUlnRemote.  # noqa: E501

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :return: The ca_cert of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this PatchedrpmUlnRemote.

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :param ca_cert: The ca_cert of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ca_cert is not None and len(ca_cert) < 1):
            raise ValueError("Invalid value for `ca_cert`, length must be greater than or equal to `1`")  # noqa: E501

        self._ca_cert = ca_cert

    @property
    def client_cert(self):
        """Gets the client_cert of this PatchedrpmUlnRemote.  # noqa: E501

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :return: The client_cert of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._client_cert

    @client_cert.setter
    def client_cert(self, client_cert):
        """Sets the client_cert of this PatchedrpmUlnRemote.

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :param client_cert: The client_cert of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                client_cert is not None and len(client_cert) < 1):
            raise ValueError("Invalid value for `client_cert`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_cert = client_cert

    @property
    def client_key(self):
        """Gets the client_key of this PatchedrpmUlnRemote.  # noqa: E501

        A PEM encoded private key used for authentication.  # noqa: E501

        :return: The client_key of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """Sets the client_key of this PatchedrpmUlnRemote.

        A PEM encoded private key used for authentication.  # noqa: E501

        :param client_key: The client_key of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                client_key is not None and len(client_key) < 1):
            raise ValueError("Invalid value for `client_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_key = client_key

    @property
    def tls_validation(self):
        """Gets the tls_validation of this PatchedrpmUlnRemote.  # noqa: E501

        If True, TLS peer validation must be performed.  # noqa: E501

        :return: The tls_validation of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: bool
        """
        return self._tls_validation

    @tls_validation.setter
    def tls_validation(self, tls_validation):
        """Sets the tls_validation of this PatchedrpmUlnRemote.

        If True, TLS peer validation must be performed.  # noqa: E501

        :param tls_validation: The tls_validation of this PatchedrpmUlnRemote.  # noqa: E501
        :type: bool
        """

        self._tls_validation = tls_validation

    @property
    def proxy_url(self):
        """Gets the proxy_url of this PatchedrpmUlnRemote.  # noqa: E501

        The proxy URL. Format: scheme://host:port  # noqa: E501

        :return: The proxy_url of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this PatchedrpmUlnRemote.

        The proxy URL. Format: scheme://host:port  # noqa: E501

        :param proxy_url: The proxy_url of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                proxy_url is not None and len(proxy_url) < 1):
            raise ValueError("Invalid value for `proxy_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._proxy_url = proxy_url

    @property
    def proxy_username(self):
        """Gets the proxy_username of this PatchedrpmUlnRemote.  # noqa: E501

        The username to authenticte to the proxy.  # noqa: E501

        :return: The proxy_username of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._proxy_username

    @proxy_username.setter
    def proxy_username(self, proxy_username):
        """Sets the proxy_username of this PatchedrpmUlnRemote.

        The username to authenticte to the proxy.  # noqa: E501

        :param proxy_username: The proxy_username of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                proxy_username is not None and len(proxy_username) < 1):
            raise ValueError("Invalid value for `proxy_username`, length must be greater than or equal to `1`")  # noqa: E501

        self._proxy_username = proxy_username

    @property
    def proxy_password(self):
        """Gets the proxy_password of this PatchedrpmUlnRemote.  # noqa: E501

        The password to authenticate to the proxy. Extra leading and trailing whitespace characters are not trimmed.  # noqa: E501

        :return: The proxy_password of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, proxy_password):
        """Sets the proxy_password of this PatchedrpmUlnRemote.

        The password to authenticate to the proxy. Extra leading and trailing whitespace characters are not trimmed.  # noqa: E501

        :param proxy_password: The proxy_password of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                proxy_password is not None and len(proxy_password) < 1):
            raise ValueError("Invalid value for `proxy_password`, length must be greater than or equal to `1`")  # noqa: E501

        self._proxy_password = proxy_password

    @property
    def username(self):
        """Gets the username of this PatchedrpmUlnRemote.  # noqa: E501

        Your ULN account username.  # noqa: E501

        :return: The username of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PatchedrpmUlnRemote.

        Your ULN account username.  # noqa: E501

        :param username: The username of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this PatchedrpmUlnRemote.  # noqa: E501

        Your ULN account password.  # noqa: E501

        :return: The password of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PatchedrpmUlnRemote.

        Your ULN account password.  # noqa: E501

        :param password: The password of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 1):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def pulp_labels(self):
        """Gets the pulp_labels of this PatchedrpmUlnRemote.  # noqa: E501


        :return: The pulp_labels of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._pulp_labels

    @pulp_labels.setter
    def pulp_labels(self, pulp_labels):
        """Sets the pulp_labels of this PatchedrpmUlnRemote.


        :param pulp_labels: The pulp_labels of this PatchedrpmUlnRemote.  # noqa: E501
        :type: dict(str, str)
        """

        self._pulp_labels = pulp_labels

    @property
    def download_concurrency(self):
        """Gets the download_concurrency of this PatchedrpmUlnRemote.  # noqa: E501

        Total number of simultaneous connections. If not set then the default value will be used.  # noqa: E501

        :return: The download_concurrency of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: int
        """
        return self._download_concurrency

    @download_concurrency.setter
    def download_concurrency(self, download_concurrency):
        """Sets the download_concurrency of this PatchedrpmUlnRemote.

        Total number of simultaneous connections. If not set then the default value will be used.  # noqa: E501

        :param download_concurrency: The download_concurrency of this PatchedrpmUlnRemote.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                download_concurrency is not None and download_concurrency < 1):  # noqa: E501
            raise ValueError("Invalid value for `download_concurrency`, must be a value greater than or equal to `1`")  # noqa: E501

        self._download_concurrency = download_concurrency

    @property
    def max_retries(self):
        """Gets the max_retries of this PatchedrpmUlnRemote.  # noqa: E501

        Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used.  # noqa: E501

        :return: The max_retries of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this PatchedrpmUlnRemote.

        Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used.  # noqa: E501

        :param max_retries: The max_retries of this PatchedrpmUlnRemote.  # noqa: E501
        :type: int
        """

        self._max_retries = max_retries

    @property
    def policy(self):
        """Gets the policy of this PatchedrpmUlnRemote.  # noqa: E501

        The policy to use when downloading content. The possible values include: 'immediate', 'on_demand', and 'streamed'. 'immediate' is the default.  * `immediate` - When syncing, download all metadata and content now. * `on_demand` - When syncing, download metadata, but do not download content now. Instead, download content as clients request it, and save it in Pulp to be served for future client requests. * `streamed` - When syncing, download metadata, but do not download content now. Instead,download content as clients request it, but never save it in Pulp. This causes future requests for that same content to have to be downloaded again.  # noqa: E501

        :return: The policy of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: PolicyEnum
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PatchedrpmUlnRemote.

        The policy to use when downloading content. The possible values include: 'immediate', 'on_demand', and 'streamed'. 'immediate' is the default.  * `immediate` - When syncing, download all metadata and content now. * `on_demand` - When syncing, download metadata, but do not download content now. Instead, download content as clients request it, and save it in Pulp to be served for future client requests. * `streamed` - When syncing, download metadata, but do not download content now. Instead,download content as clients request it, but never save it in Pulp. This causes future requests for that same content to have to be downloaded again.  # noqa: E501

        :param policy: The policy of this PatchedrpmUlnRemote.  # noqa: E501
        :type: PolicyEnum
        """

        self._policy = policy

    @property
    def total_timeout(self):
        """Gets the total_timeout of this PatchedrpmUlnRemote.  # noqa: E501

        aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The total_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: float
        """
        return self._total_timeout

    @total_timeout.setter
    def total_timeout(self, total_timeout):
        """Sets the total_timeout of this PatchedrpmUlnRemote.

        aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param total_timeout: The total_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                total_timeout is not None and total_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `total_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._total_timeout = total_timeout

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this PatchedrpmUlnRemote.  # noqa: E501

        aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The connect_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: float
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this PatchedrpmUlnRemote.

        aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param connect_timeout: The connect_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                connect_timeout is not None and connect_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `connect_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._connect_timeout = connect_timeout

    @property
    def sock_connect_timeout(self):
        """Gets the sock_connect_timeout of this PatchedrpmUlnRemote.  # noqa: E501

        aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The sock_connect_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: float
        """
        return self._sock_connect_timeout

    @sock_connect_timeout.setter
    def sock_connect_timeout(self, sock_connect_timeout):
        """Sets the sock_connect_timeout of this PatchedrpmUlnRemote.

        aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param sock_connect_timeout: The sock_connect_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                sock_connect_timeout is not None and sock_connect_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `sock_connect_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._sock_connect_timeout = sock_connect_timeout

    @property
    def sock_read_timeout(self):
        """Gets the sock_read_timeout of this PatchedrpmUlnRemote.  # noqa: E501

        aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The sock_read_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: float
        """
        return self._sock_read_timeout

    @sock_read_timeout.setter
    def sock_read_timeout(self, sock_read_timeout):
        """Sets the sock_read_timeout of this PatchedrpmUlnRemote.

        aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param sock_read_timeout: The sock_read_timeout of this PatchedrpmUlnRemote.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                sock_read_timeout is not None and sock_read_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `sock_read_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._sock_read_timeout = sock_read_timeout

    @property
    def headers(self):
        """Gets the headers of this PatchedrpmUlnRemote.  # noqa: E501

        Headers for aiohttp.Clientsession  # noqa: E501

        :return: The headers of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: list[object]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this PatchedrpmUlnRemote.

        Headers for aiohttp.Clientsession  # noqa: E501

        :param headers: The headers of this PatchedrpmUlnRemote.  # noqa: E501
        :type: list[object]
        """

        self._headers = headers

    @property
    def rate_limit(self):
        """Gets the rate_limit of this PatchedrpmUlnRemote.  # noqa: E501

        Limits requests per second for each concurrent downloader  # noqa: E501

        :return: The rate_limit of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """Sets the rate_limit of this PatchedrpmUlnRemote.

        Limits requests per second for each concurrent downloader  # noqa: E501

        :param rate_limit: The rate_limit of this PatchedrpmUlnRemote.  # noqa: E501
        :type: int
        """

        self._rate_limit = rate_limit

    @property
    def uln_server_base_url(self):
        """Gets the uln_server_base_url of this PatchedrpmUlnRemote.  # noqa: E501

        Base URL of the ULN server. If the uln_server_base_url is not provided pulp_rpm willuse the contents of the DEFAULT_ULN_SERVER_BASE_URL setting instead.  # noqa: E501

        :return: The uln_server_base_url of this PatchedrpmUlnRemote.  # noqa: E501
        :rtype: str
        """
        return self._uln_server_base_url

    @uln_server_base_url.setter
    def uln_server_base_url(self, uln_server_base_url):
        """Sets the uln_server_base_url of this PatchedrpmUlnRemote.

        Base URL of the ULN server. If the uln_server_base_url is not provided pulp_rpm willuse the contents of the DEFAULT_ULN_SERVER_BASE_URL setting instead.  # noqa: E501

        :param uln_server_base_url: The uln_server_base_url of this PatchedrpmUlnRemote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                uln_server_base_url is not None and len(uln_server_base_url) < 1):
            raise ValueError("Invalid value for `uln_server_base_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._uln_server_base_url = uln_server_base_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchedrpmUlnRemote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedrpmUlnRemote):
            return True

        return self.to_dict() != other.to_dict()
