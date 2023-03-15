---
title: User Access APIs
layout: default
nav_link: User Access APIs
nav_order: 410
nav_level: 2
lang: en
---
# <a name="userGroup" class="api-ref-title">User Access APIs</a>
An application can use the User Management API to access Adobe users and manage their identities.

## Retrieving Users

You can list all users, retrieve information for individual users, and list members of user groups and product profile groups.

* [List all users](getUsersWithPage.md) : `GET /v2/usermanagement/users/{orgId}/{page}`
* [Get user information](getUser.md) : `GET /v2/usermanagement/organizations/{orgId}/users/{userString}`
* [Get all member users in a group](getUsersByGroup.md) : `GET /v2/usermanagement/users/{orgId}/{page}/{groupName}`

## User Actions

You can create and remove user accounts for your organization, modify a user’s personal information (depending on the account type).

Request these user-management actions for your organization using the [`action` API](ActionsRef.md). 
```
POST v2/usermanagement/action/{orgId}
```

The _commands_ in the body of your POST request specify _action steps_ to take for a given _user_.

* Create or add a user to an organization
 + [addAdobeId](ActionsCmds.md#addAdobeID) Create or add an Adobe ID user
 + [createEnterpriseID](ActionsCmds.md#createEnterpriseID) Create an Enterprise ID user
 + [createFederatedID](ActionsCmds.md#createFederatedID) Create an Federated ID user.
* [update](ActionsCmds.md#update) Update an existing user in an organization
* [remove](ActionsCmds.md#removeFromOrg) Remove a user from an organization

You can also use `action` requests to modify users' memberships and administrative roles. See [User Group APIs](group.md) for details.

<hr class="api-ref-rule">
