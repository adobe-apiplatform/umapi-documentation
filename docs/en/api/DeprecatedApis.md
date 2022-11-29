---   
title: Deprecated APIs    
layout: default   
nav_link: Deprecated APIs   
nav_order: 430    
nav_level: 2    
lang: en    
---  

# Deprecated APIs

The following APIs have been deprecated. These APIs will continue to function but could be removed at some point in the future.  Their usage is strongly discouraged.  Alternatives are noted below.

| Deprecated | Current |
| :--- | :------ |
| Get All Users through [GET /v2/usermanagement/{orgId}/users](getUsersREST.md)| _See [Get Users in Organization](getUsersWithPage.md)_ |
| Separate [User Group APIs](usergroup.md) and [Product Information APIs](product.md) | _See [Get Groups and Product Profiles](group.md)_ |
| [GET /v2/usermanagement/organizations/{orgId}/users/{userString}](getUser.md) | The `adminRoles` property is now deprecated, and administrative roles are reflected in group memberships, returned in the [`groups`](getUser.md#ResponseProps) field. |
| [GET /v2/usermanagement/users/{orgId}/{page}](getUsersWithPage.md) | The `adminRoles` property is now deprecated, and administrative roles are reflected in group memberships, returned in the [`groups`](getUsersWithPage.md#ResponseProps) field. |
| [GET /v2/usermanagement/users/{orgId}/{page}/{groupName}](getUsersByGroup.md) | The `adminRoles` property is now deprecated, and administrative roles are reflected in group memberships, returned in the [`groups`](getUsersByGroup.md#ResponseProps) field. |
{:.bordertablestyle}

>Please note that some additional properties can appear in a response but should not be relied upon. Only rely on those properties that are documented in the Response Properties section for each API.