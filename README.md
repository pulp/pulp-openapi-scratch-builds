# Scratch builds Pulp client bindings from pulp-openapi-generator with Domain support enabled

Needed because the builds on PyPI do not have domain support enabled currently

# License:

GPLv2+

# Example command for building them

After downloading pulp-openapi-generator and the repo for the plugin:

```
PULP_URL=https://console.redhat.com PULP_API_ROOT=/api/pulp/ ./generate.sh pulp_ostree python
```
