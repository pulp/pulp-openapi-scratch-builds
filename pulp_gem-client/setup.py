# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "pulp_gem-client"
VERSION = "0.6.2"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.1, < 2.10.0",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Pulp 3 API",
    author="Pulp Team",
    author_email="pulp-list@redhat.com",
    url="",
    keywords=["pulp", "pulpcore", "client", "Pulp 3 API"],
    install_requires=REQUIRES,
    python_required=PYTHON_REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="GPLv2+",
    long_description_content_type='text/markdown',
    long_description="""\
    Fetch, Upload, Organize, and Distribute Software Packages
    """,  # noqa: E501
    package_data={"pulpcore.client.pulp_gem": ["py.typed"]},
)
