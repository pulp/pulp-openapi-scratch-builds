# Repair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_checksums** | **bool** | Will verify that the checksum of all stored files matches what saved in the database. Otherwise only the existence of the files will be checked. Enabled by default | [optional] [default to True]

## Example

```python
from pulpcore.client.pulp_rpm.models.repair import Repair

# TODO update the JSON string below
json = "{}"
# create an instance of Repair from a JSON string
repair_instance = Repair.from_json(json)
# print the JSON string representation of the object
print(Repair.to_json())

# convert the object into a dict
repair_dict = repair_instance.to_dict()
# create an instance of Repair from a dict
repair_from_dict = Repair.from_dict(repair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


