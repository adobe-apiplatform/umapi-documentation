---
title: API Reference
layout: page
nav_link: API Reference
nav_order: 410
nav_level: 1
lang: en
---

{% include umIntro.md %}

* [Connecting to the User Management API](#connect)
* [API Reference]()
    * [Create and Add Users](#add)
    * [Update User Records](#update)
    * [Remove Users](#remove)
    * [Access Users](#users)
    * [Manage User Groups](#usergroups)
    * [Access Products and Product Profiles](product.html)
    * [Provision Users](#provision)
    * [Manage Administrators](#admin)

# <a name="connect" class="api-ref-subtitle">Connecting to the User Management API</a>

To establish a secure user-management session, you create a [JSON Web Token]() that encapsulates your identity information and exchange it for an access token. Please see the [Prerequisites](../getstarted.html#prereq) section of the [Getting Started Guide](../getstarted.html) for detailed information of obtaining this access token.

* A typical access token is valid for 24 hours after it is issued.
* You can request multiple access tokens. Previous tokens are not invalidated when a new one is issued. You can authorize requests with any valid access token. This allows you to overlap access tokens to ensure your integration is always able to connect to Adobe.

Every call to the User Management API endpoints must be authorized with this access token in the `Authorization` header, along with the _API key_ you created when you created the integration in the [Adobe I/O Console](https://console.adobe.io/).

For an example of a Python script that creates a JWT and exchanges it for an _access token_, see the [User Management Walkthrough](../samples/index.html).

# User Management API Reference

An application can use the User Management API to access Adobe users and manage their identities. You can create and remove user accounts for your organization, modify a user's personal information (depending on the account type), and modify users' access rights to Adobe applications within your organization.

Address all user-management requests to the UM API server:

```
https://usermanagement.adobe.io/v2/usermanagement/...
```

## <a name="add" class="api-ref-subtitle">Create and Add Users</a>

{% include manageUsers.md %}

The POST [action](ActionsRef.html) API allows an Organization to create or add users to an organization by specifying a _command_ in the request body. The following links detail the commands but it is recommended to read the full [API reference](ActionsRef.html) first.

* [Add an Adobe ID to your organization](ActionsRef.html#addAdobeID)
* [Create an Adobe-hosted Enterprise ID for your organization](ActionsRef.html#createEnterpriseID)
* [Create a Federated ID in a domain owned by your organization.](ActionsRef.html#createFederatedID)

## <a name="update" class="api-ref-subtitle">Update Users</a>

You can update personal information for a user who has an Enterprise or Federated ID that is managed by your organization through the POST [action](ActionsRef.html) API using the _update command_ in the request body. The following link details the command but it is recommended to read the full [API reference](ActionsRef.html) first.

* [Update an Enterprise or Federated user](ActionsRef.html#update)

## <a name="remove" class="api-ref-subtitle">Remove Users</a>

UM API allows an organization to remove a user from an organization, or from a Trusted Domain through the POST [action](ActionsRef.html) API. The _removeFromOrg command_ removes the user from the organization and from any product profiles and user-groups in the organization. An organization can also delete user accounts of type Enterprise and Federated ID, if the caller is from the owning organization and has delete access. This will also remove them from all product profiles and user-groups in a given domain.

* [Remove a user from the organization](ActionsRef.html#removeFromOrg)

## <a name="users" class="api-ref-subtitle">Access Users</a>

The retrieval of users and membership details in user-groups and product profiles are available through the following GET APIs:

* [Get all users in an organization](getUsers.html#getUsers)
* [Get a user](getUsers.html#getUserByEmailOrUsername)
* [Get all users in a user-group](getUsersByGroup.html#getUsersByGroup)
* [Get all users in a product profile](getUsersByGroup.html#getUsersByGroup)

## <a name="usergroups" class="api-ref-subtitle">Manage User-Groups</a>

User Management provides an API user-groups retrieval. Through the POST [action](ActionsRef.html) API we also enable management of group membership and assignment of administrators:

<!-- * [Create a user-group](usergroup.html#createUserGroup)
* [Update a user-group](usergroup.html#updateUserGroup)
* [Delete a user-group](usergroup.html#deleteUserGroup) 
* [Get all user-groups in an Organization](usergroup.html#getUserGroups)
* [Get details of a particular user-group](usergroup.html#getUserGroup) -->
* [Add a user to a user-group](ActionsRef.html#add)
* [Remove a user from a user-group](ActionsRef.html#remove)
* [Add User-group Administrator permissions to a user](ActionsRef.html#addRoles)
* [Remove User-group Administrator permissions to a user](ActionsRef.html#removeRoles)
* [Get a list of users in a user-group](getUsersByGroup.html)

## <a name="provision" class="api-ref-subtitle">Provision Users</a>

{% include manageProductAccess.md %}

The POST [action](ActionsRef.html) API allows an Organization to add and remove users from User-Groups and Product Profiles by specifying a _command_ in the request body. The following links detail the commands but it is recommended to read the full [API reference](ActionsRef.html) first.

* [Provision a user to a product profile](ActionsRef.html#add)
* [Remove provisioning of a user from a product profile](ActionsRef.html#remove)
* [Add a user-group to a product profile](ActionsRef.html#add)
* [Remove a user-group from a product profile](ActionsRef.html#remove)
* [Add a user to a user-group](ActionsRef.html#add)
* [Remove a user from a user-group](ActionsRef.html#remove)

## <a name="admin" class="api-ref-subtitle">Manage Administrators</a>

UM API enables an organization to manage administrative rights.{% include apiRef/rolesDescription.md %}

The POST [action](ActionsRef.html) API uses the _addRoles_ and _removeRoles_ commands to manage administrator rights:

* [Add System Administrator permissions to a user](ActionsRef.html#addRoles)
* [Remove System Administrator permissions to a user](ActionsRef.html#removeRoles)
* [Add Deployment Administrator permissions to a user](ActionsRef.html#addRoles)
* [Remove Deployment Administrator permissions to a user](ActionsRef.html#removeRoles)
* [Add Product Administrator permissions to a user](ActionsRef.html#addRoles)
* [Remove Product Administrator permissions to a user](ActionsRef.html#removeRoles)
* [Add Product Profile Administrator permissions to a user](ActionsRef.html#addRoles)
* [Remove Product Profile Administrator permissions to a user](ActionsRef.html#removeRoles)
* [Add User-group Administrator permissions to a user](ActionsRef.html#addRemoveRoleAttr)
* [Remove User-group Administrator permissions to a user](ActionsRef.html#addRemoveRoleAttr)
