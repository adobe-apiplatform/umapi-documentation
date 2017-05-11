---
layout: page
title: Creating User Management Applications
advertise: Create Apps
---

# Creating User Management Applications

To obtain the credentials you need to access the User Management service, create a **Service Account Integration** using the [Adobe I/O Console](https://console.adobe.io/). To establish a secure service-to-service API session, you will create a JSON Web Token (JWT) that encapsulates your integration credentials, and exchange it for an access token. Every request to an Adobe service must include the access token in the **Authorization** HTTP header, along with the API Key (client  ID) that was generated when you created the integration.

For complete details of the entire integration process, see [Service Account Authentication](https://www.adobe.io/apis/cloudplatform/console/authentication/jwt_workflow.html).

Address all user-management requests to the UM API server:

```
https://usermanagement.adobe.io/v2/usermanagement/...
```

**NOTE:** In syntax statements, this address is shortened to **[UM_Server]**.

There are separate endpoints under the user-management server for write operations (managing the enterprise user base), and read operations (retrieving information from the enterprise user base). The API defines a set of specific write actions that you can use to create, update, and delete user accounts, and manage Adobe product access for users. The read operations retrieve information about users and product configurations in your organization.

***

* [Authorization](#authorization)
* [Manage your Adobe Users](#manage-your-adobe-users)
* [Query your Adobe Users and Product Access](#query-your-adobe-users-and-product-access)

For a Python code walkthrough and samples of actual API calls, see the [User Management Walkthrough](samples/index.md).

***

## Authorization

All requests to the User Management service must be made using the HTTPS secure protocol and authorized with a current access token and your API key. Include these headers in all requests:

* **Authorization** : A current access token obtained from the login request.
* **x-api-key** : The API key for your integration.

To gain access to the service, you must create a JSON Web Token (JWT) that encapsulates your client credentials, and sign the JWT with the private key for a public-key certificate associated with the integration. For complete details, see [Creating a JSON Web Token](https://www.adobe.io/apis/cloudplatform/console/authentication/createjwt.html). 

We recommend that you store your API client credentials and private key with strong protection, but that you do NOT store a JWT or access token. You should create a new JWT for each user-management session, and use it to obtain an access token for that session.

### Log in to gain API access

To initiate each user-management session, create and send a JSON Web Token to Adobe in an access request. Include your JWT in a POST request to the Adobe Identity Management Service (IMS):
```
        https://ims-na1.adobelogin.com/ims/exchange/jwt/
```
Pass the signed, base-64 encoded JWT as the value of the URL-encoded **jwt_token** parameter in the body of the POST request.

The response contains an access token that is valid for 24 hours after it is issued. Pass this token in the **Authorization** header in all subsequent requests to the User Management API.

You can request multiple access tokens. Previous tokens are not invalidated when a new one is issued. You can authorize requests with any valid access token. This allows you to overlap access tokens to ensure your integration is always able to connect to Adobe.

* For details of the log-in call, see [JWT Authentication Reference](https://www.adobe.io/apis/cloudplatform/console/authentication/connect.html).
* For an example of a script that creates a JWT and makes a log-in call, see [User Management Walkthrough.](samples/index.md)

***

## Manage your Adobe Users

Call the user-management API to request changes to your Adobe user accounts.

* You can create new accounts for account types Enterprise ID and Federated ID, and you can invite users to join your organization with account type Adobe ID.<br>
For the Adobe ID account type, the user is identified by email and an email invite is sent. The Adobe ID can already exist or be created after the invite is accepted.
* You can manage pending new-user invites.
* You can update the user information associated with an Enterprise ID or Federated ID account that is managed by your organization.
* You can manage product access and user-group membership for users.
* You can delete accounts from your organization.
* You can initiate password reset for Enterprise ID users.

### Making user-management requests

To make most user-management requests, connect to this URL:

```
[UM_Server]/action/{orgId}
```

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".

Send POST requests whose body contains a JSON structure that specifies a set of commands. Each command names a user, and specifies one or more actions to take on that user's account. A single request can include commands for multiple users.

**Available operations**

| Operation | Function |
| --- | --- |
| **createEnterpriseID** | Create an Adobe-hosted Enterprise ID for your organization. |
| **createFederatedID** | Create a Federated ID in a domain owned by your organization. |
| **addAdobeID** | Issue an invitation to a user with a general Adobe ID to join your organization.The user receives an email with a link for accepting the invitation. Users do not become members of your organization until they accept. You cannot perform any other steps for a user with a pending invitation, such as adding product accesss. |
| **update** | Update personal information for a user who has an Enterprise or Federated ID that is managed by your organization. |
| **add**, **remove** | Manage product access.You must create Product Configurations in the [Admin Console](https://adminconsole.adobe.com/enterprise/), and assign each one a unique identifing nickname. You can then use the User Management API to manage product access for user by adding and removing users to and from your existing product configurations. |
| **addRoles**, **removeRoles** | Add or remove a user's admin rights for specific user-groups, products, and defined Product Configurations. |
| **removeFromOrg removeFromDomain** | Remove the user from the organization, or from a Trusted Domain.-- **removeFromOrg**removes the user from the organization and from any product configurations in the organization.-- **removeFromDomain**removes the user from all product configurations for that domain.For user accounts of type Enterprise and Federated ID, if the caller is from the owning organization and has delete access, **removeFromDomain**also deletes the user account.If the user is specified by email address, then the domain of the email address specifies the domain of the account. If the user is specified by Username, the domain must be provided. |
| **resetPassword** | For Enterprise IDs only, initiates the password-reset process for the user.Sends a password-reset email, and prevents login to the account until the password is reset. |

### Managing User Invites

When you add a user with the Adobe ID type to join your organization, they get an email invitation. To manage pending invites, send a POST or DELETE request to this URL:

```
[UM_Server]/{orgId}/invites/{email}
```

***

### Managing Administrative Access

To manage administrative rights for user groups, products, or product configurations, send the POST request to one of these URLs:

```
   [UM_Server]/{orgId}/user-groups/{userGroupId}
   [UM_Server]/{orgId}/products/{productId}
   [UM_Server]/{orgId}/products/{productId}/configurations/{configId}
```

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".
* Replace the **{...Id}** elements with the unique IDs assigned to user groups, products, and product configurations that are defined for you organization.

***

### For More Information

For detailed descriptions and examples of specific user-management operations, see the following pages.

* For specific request and response syntax, see [Managing Users](api/ManageRef.md).
* For detailed syntax of the JSON commands structure and user account operations, see [User Management Actions](api/ActionsRef.md).
* For examples of user-management requests, see:
  - [Create users](samples/SampleCreate.md)
  - [Manage pending invites](samples/SampleInvites.md)
  - [Update user information](samples/SampleUpdate.md)
  - [Add and remove membership and admin rights in user groups](samples/SampleGroups.md)<br>
  - [Add and remove entitlements through product configuration membership](samples/SampleGroups.md)
  - [Remove users](samples/SampleRemove.md)
  - [Perform multiple actions for one user](samples/SampleMultiActions.md)
  - [Perform actions for multiple users](samples/SampleMultiUser.md)

***

## Query your Adobe Users and Product Access

You can retrieve paged lists of all users and products for the organization, and of user groups and product configurations that you have defined in the [Admin Console](https://adminconsole.adobe.com/enterprise/). Product configurations are identified by the nickname you have assigned to them in the Admin Console. You can then examine an individual user, user group, product, or product configuration using its unique ID.

There are API endpoints for each resource type under your organization's unique ID. For example, to list users in your existing user base and get the information for a particular user, send GET requests to these URLs:

```
   GET [UM_Server]/{orgId}/users/
   GET [UM_Server]/{orgId}/users/{userId}
```

For compatability with previous releases, you can also access information through endpoints that use the _resource_type/orgID_ structure. For example:

```
   GET [UM_Server]/users/{orgId}/
```

When you invite users with the Adobe ID type to join your organization, they are not added to the list of users until they accept the email invite. To list and get information about pending new-user invites, send a GET request to the _invites_ resource:

```
   GET [UM_Server]/{orgId}/invites/
   GET [UM_Server]/{orgId}/invites/{email}
```

* For specific endpoints and request/response syntax, see [Query API Reference](api/QueryRef.md)
* For examples of user-base query requests, see [Query user information](samples/SampleQuery.md)
