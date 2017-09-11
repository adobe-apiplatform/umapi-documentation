# Adobe: User Management API: ErrorCodes

| ErrorCode | Description | Operation|
| ---- | --------------- | ---- |
| error.apikey.invalid | Organization’s API key is not valid | all APIs |
| error.group.invalid_list | | createEnterpriseID, createFederatedID |
| error.internal.create_failed | Operation failed for unknown reason. | create |
| error.internal.update_failed | Operation failed for unknown reason. | update |
| error.internal.removefromorg | Operation failed for unknown reason. | removeFromOrg |
| error.organization.invalid_id | The organization ID provided is invalid | all APIs |
| error.organization.migrating | Returned if the organization is in a migrating state. Changes cannot be made to an org when it is migrating. Migration can be part of the EVIP workflows or OneConsole. | all APIs |
| error.update.adobeid.no | The operation in the command cannot be applied to an Adobe ID. | update |
