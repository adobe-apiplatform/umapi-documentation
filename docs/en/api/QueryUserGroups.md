---
layout: default
nav_link: Get User Group Users and Admins
nav_order: 447
nav_level: 3
lang: en
title: Get User Group Users and Admins
---

User group information defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/) is available through the **{orgId}/user-groups** resource.

* [Get a paged list of user groups defined for your organization](usergroup.html#getUserGroups)
* [Get information for a specific user group](usergroup.html#getUserGroup)
* [Get a paged list of users or admins users who belong to a specific user group](#users)

### Notation

In syntax statements for endpoints, the following notation is used:

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Curly braces indicate a variable, to be replaced with specific values for your organization.
  - Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".
  - Replace **{groupId}** with the unique ID or name assigned to user groups that are defined for you organization.
  - Replace the **{page}** element with the zero-based index for the first requested page of the paged result.
  
### Request headers

You must include these headers in all requests:

* **Authorization** : A current access token obtained from login request.
* **x-api-key** : The API key for your organization, obtained from the Developer Portal.

## <a name="users" class="api-ref-subtitle">List Users in a User Group</a>

A GET request to the **/users** or **/admins** endpoint under a specific user group retrieves a paged list of users who belong to the group, or of users with the administrative role for the group.

```
GET [UM_Server]/{orgId}/user-groups/{groupId}/users[?page={n}]
GET [UM_Server]/{orgId}/user-groups/{groupId}/admins[?page={n}]
```

* **{orgId}** : Required. The unique ID of your organization.
* **{groupId}** : Required. The unique ID of the user group.
* **page={n}** : Optional. A zero-based index into the start entry of the paged response. Default is 0

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user data in JSON format:

```json
[
  {
    "email": "admin1@domain6.us",
    "firstName": "admin1",
    "lastName": "domain6",
    "countryCode": "US",
    "status": "active",
    "userType": "federatedID"
   },
  {
    "email": "anksharm@adobe.com",
    "firstName": "ankush",
    "lastName": "kumar",
    "countryCode": "IN",
    "status": "active",
    "userType": "adobeID"
   },
   ...
  ]
```
