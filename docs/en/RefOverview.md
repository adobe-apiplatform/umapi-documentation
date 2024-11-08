---
title: API Reference
layout: page
nav_link: API Reference
nav_order: 300
nav_level: 1
lang: en
---

{% include_relative partials/umIntro.md %}

* [Connecting to the User Management API](#connect)
* [User Management Calls](#user-management-calls)

## <a name="connect" class="api-ref-subtitle">Connecting to the User Management API</a>

To establish a secure user-management session, you create a JSON Web Token (JWT) that encapsulates your identity information and exchange it for an IMS access token. Please see the [Prerequisites](getstarted.md#prereq) section of the [Getting Started Guide](getstarted.md) for detailed information about obtaining an access token.

* A typical access token is valid for 24 hours after it is issued.
* You can request multiple access tokens. Previous tokens are not invalidated when a new one is issued. You can authorize requests with any valid access token. This allows you to overlap access tokens to ensure your integration is always able to connect to Adobe.

Every call to the User Management API endpoints must be authorized with this access token in the `Authorization` header, along with the _API key_ for your client, which you received when you created the integration in the [Adobe I/O Console](https://console.adobe.io/).

For an example of a Python script that creates a JWT and exchanges it for an _access token_, see the [User Management Walkthrough](samples/index.md).

***********

## <a name="user-management-calls" class="api-ref-subtitle">User Management API Calls</a>

An application can use the User Management API to access Adobe users and manage their identities. You can create and remove user accounts for your organization, modify a user's personal information (depending on the account type), and modify users' access rights to Adobe applications within your organization.

Address all user-management requests to the UM API server:

```
https://usermanagement.adobe.io/v2/usermanagement/...
```

<strong>NOTE:</strong> In responses, as per the [HTTP specification](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers), HTTP header names are case insensitive. For example, <code>x-current-page</code> is identical to <code>X-Current-Page</code>.

************

### Summary of Actions on Users

| Task | Operation | Endpoint | Description |
| :--- | :--- | :---| :---------- |
| [Create and Add Users](#add) | POST | `action/{orgId}`  | Create or add users to an organization by specifying a _command_ in the request body.  |
| [Update User Records](#update) | POST | `action/{orgId}`  | Update existing user records  |
| [Remove Users](#remove) |  POST | `action/{orgId}`  | Remove users from your organization |
| [Access Users](#users) | GET | various endpoints | List users in organization or in group, get individual user records  |
{:.bordertablestyle}

#### <a name="add" class="api-ref-subtitle">Create and Add Users</a>

{% include_relative partials/manageUsers.md %}

The POST [action](api/ActionsRef.md) API allows an Organization to create or add users to an organization by specifying a _command_ in the request body.

* For syntax details of the POST request and response, see [User Management Action Requests](api/ActionsRef.md).
* For details of the JSON command structure and defined actions, see [User Management Action Commands](api/ActionsCmds.md).
  + [Add an Adobe ID to your organization](api/ActionsCmds.md#addAdobeID)
  + [Create an Adobe-hosted Enterprise ID for your organization](api/ActionsCmds.md#createEnterpriseID)
  + [Create a Federated ID in a domain owned by your organization.](api/ActionsCmds.md#createFederatedID)

#### <a name="update" class="api-ref-subtitle">Update Users</a>

You can update personal information for a user who has an Enterprise or Federated ID that is managed by your organization through the POST [action](api/ActionsRef.md) API using the _update command_ in the request body. The following link details the command but it is recommended to read the full [API Actions Reference](api/ActionsRef.md) first.

* [Update an Enterprise or Federated user](api/ActionsCmds.md#update)

#### <a name="remove" class="api-ref-subtitle">Remove Users</a>

You can remove a user from your organization, or from a Trusted Domain, through the POST [action](api/ActionsRef.md) API. The _removeFromOrg command_ removes the user from the organization and from any product profiles, user groups, and administrative groups in the organization. An organization can also delete user accounts of type Enterprise and Federated ID, if the caller is from the owning organization and has delete access. This will also remove them from all groups in a given domain.

* [Remove a user from the organization](api/ActionsCmds.md#removeFromOrg)

#### <a name="users" class="api-ref-subtitle">Access Users</a>

Retrieve user information for an organization or for members of user-groups and product profiles through the following GET APIs:

* [Get all users in an organization](api/getUsersWithPage.md)
* [Get a user](api/getUser.md)
* [Get users in a group or profile](api/getUsersByGroup.md)

## Summary of Actions on Groups

Groups include user groups, product profiles, organization-wide administrative groups, and administrative groups associated with specific products, user groups, and product profiles.

* To list all types of groups, send a GET request to the  `groups/{orgId}/{page}` endpoint.
  + [Get all user groups in an Organization](api/QueryUserGroups.md)  
* To retrieve information about a particular group, send a GET request to `users/{orgId}/{page}/{groupName}`:
  + [Get details of a particular group](api/group.md)
  + [Get a list of users in a group](api/getUsersByGroup.md)
 
You can manage user groups and user-group memberships with a POST request to the `actions/{orgId}` endpoint, using the  _usergroup_ root command in the _commands_ structure. 
* [Manage user groups](api/usergroupActionCommands.md#user-group-information) with the _createUserGroup_, _deleteUserGroup_, and _updateUserGroup_ actions for a _usergroup_.
* [Add or remove user-group members](api/usergroupActionCommands.md#addRemove) with the _add_ and _remove_ actions for a _usergroup_. You can add and remove individual users and product profiles.

## <a name="admingroups" class="api-ref-subtitle">Manage Entitlements and Administrative Rights</a>

Use a POST [action](api/ActionsRef.md) request to manage entitlements and administrative rights. Entitlements are granted through membership in product profiles, and administrative rights are granted through membership in the specially named administrative groups.   

### <a name="provision" class="api-ref-subtitle">Manage Entitlements</a>

{% include_relative partials/manageProductAccess.md %}

Use the POST [action](api/ActionsRef.md) API to manage entitlements by adding and removing users to and from user groups and product profiles. 

You can give users access to a product directly by adding them to a product profile for that product,
or indirectly by adding them to a user group which itself has been added to a product profile for that product.
In either case, a user might not get access if there are not enough licenses or other resources. You can tell if access was granted by using the status parameter to [get users by group](api/getUsersByGroup.md) and see if the user is listed for the product profile. 

* [Add a user to a product profile](api/ActionsCmds.md#add)
* [Remove a user from a product profile](api/ActionsCmds.md#remove)
* [Add a user group to a product profile](api/usergroupActionCommands.md#addRemove)
* [Remove a user group from a product profile](api/usergroupActionCommands.md#addRemove)

### <a name="adminAccess" class="api-ref-subtitle">Manage Administrative Permissions</a>

Use the POST [action](api/ActionsRef.md) API to manage permissions by adding and removing users to and from administrative groups. There are three administrative groups with fixed names:

* Administrators: `_org_admin`
* Support Administrators: `_support_admin`
* Deployment Administrators: `_deployment_admin`

In addition, there are administrative groups for each user group and product profile. These are named with a prefix and the group name. For example, `_admin_Marketing`, `_developer_Marketing` or `_product_admin_Adobe Document Cloud for business`.

Please note that you cannot assign or remove the administrative role `_org_admin` using User Management API.

* [Add Administrator permissions for a user](api/ActionsCmds.md#add) with the _add_ action for a _user_
* [Remove Administrator permissions for a user](api/ActionsCmds.md#remove) with the _remove_ action for a _user_
