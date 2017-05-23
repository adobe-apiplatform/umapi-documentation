---
title: API Reference
layout: page
nav_link: API Reference
nav_order: 50
nav_level: 1
lang: en
---

# User Management API Reference

An application can use the User Management API to access Adobe users and manage their identities. You can create and remove user accounts for your organization, modify a user's personal information (depending on the account type), and modify users' access rights to Adobe applications within your organization.

***

## User Management Login

To access the user-management service, you must exchange your API key and credentials for an API access token. To initiate each user-management session, send a request to the Login endpoint.

```
https://ims-na1.adobelogin.com/ims/exchange/jwt
```

See [Access API Reference](ConnectAPIRef.md) for complete syntax details.

## User Management Resources

Address all user-management requests to the UM API server:

```
https://usermanagement.adobe.io/v2/usermanagement/...
```

In syntax statements, this address is shortened to **[UM_Server]**.

Resource endpoints allow you to create users, request changes to user records and product access, and make read-only queries for user information.

Access to your own organization's users is available through the organization ID that you are assigned on registration. In syntax statements, this is represented as **{orgId**}. Replace this element with with your organization's unique ID, which looks like this: "12345@AdobeOrg".

### [Write operations](ManageRef.md)

To request most user-management actions, send POST requests to the **action** endpoint for your organization.

```
[UM_Server]/action/{orgId}
```

The requested action is contained in a **commands** structure in the JSON body of the request. See [User Management Resource Reference](ManageRef.md) for complete syntax details.

In addition, you can update administrative rights for user groups, products, and product configurations with POST requests to these endpoints:

```
   [UM_Server]/{orgId}/user-groups/{userGroupId}
   [UM_Server]/{orgId}/products/{productId}
   [UM_Server]/{orgId}/products/{productId}/configurations/{configId}
```

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".
* Replace the **{...Id}** elements with the unique IDs assigned to user groups, products, and product configurations that are defined for your organization.

### [Read operations](QueryRef.md)

To retrieve user and product configuration information for your organization, send GET requests to endpoints for your organization. There are endpoints for users, user-groups, products, and product configurations under your own organization's endpoint. For example, **[UM_Server]/{orgId}/users**.

NOTE: There are also endpoints for your organization under **users/**, **groups/**, and **organizations/**; for example, **[UM_Server]/users/{orgId}/{page}**. This usage is supported for compatability, but may be deprecated in future.

See [User Query Resource Reference](QueryRef.md) for complete syntax details.
