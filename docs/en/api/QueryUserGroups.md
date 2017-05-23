---
layout: default
nav_link: Accessing User Group Information
nav_order: 700
nav_level: 2
lang: en
---

# Accessing User Group Information

User group information defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/) is available through the **{orgId}/user-groups** resource.

* Get a paged list of user groups defined for your organization:

```
GET [UM_Server]/{orgId}/user-groups
```
* Get information for a specific user group:

```
GET [UM_Server]/{orgId}/user-groups/{groupId}
```
* Get a paged list of users or admins users who belong to a specific user group:

```
GET [UM_Server]/{orgId}/user-groups/{groupId}/users
GET [UM_Server]/{orgId}/user-groups/{groupId}/admins
```

***

## List User Groups

A GET request to the **/{orgId}/user-groups** resource retrieves a paged list of user groups that have been defined for your organization.

```json
GET [UM_Server]/{orgId}/user-groups[?page={n}]
```

* **{orgId}** : Required. The unique ID of your organization.
* **page={n}** : Optional. A zero-based index for the start entry of the paged response. Default is 0.

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user-group data in JSON format:

```json
[
    {
        "groupId": 28813981,
        "name": "UMSDK User Group",
        "type": "USER_GROUP",
        "userCount": 0
    },
    {
        "groupId": 28813990,
        "name": "UMSDK User Group 2",
        "type": "USER_GROUP",
        "userCount": 0
    },
    {
        "groupId": 28813993,
        "name": "UMSDK User Group 3",
        "type": "USER_GROUP",
        "userCount": 0
    }
]
```

A failed request can result in a response with one of these HTTP status values, with an error message in the response body:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.
* **403 Forbidden** : x-api-key header is missing.
* **404 Not Found** : groupId was not found.

_Note that server errors can occur that require exponential back-off on retry._

***

## Examine a User Group

A GET request to the **{orgId}/user-groups/{groupId}** resource retrieves the configuration information for an individual user group. The body of the response contains the user information in JSON format.

```json
   GET [UM_Server]/{orgId}/user-groups/{groupId}
```

* **{orgId}** : Required. The unique ID of your organization.
* **{groupId}** : Required. The unique ID of the user group.

### Responses

A successful request returns the requested data with **HTTP status 200**. The response body contains the requested user-group data in JSON format.

```json
{ "groupId": 3871445, "name": "Marketing Reports & Analytics", "type": "USER_GROUP", "userCount": 5 }
```

***

## List Users in a User Group

A GET request to the **/users** or **/admins** endpoint under a specific user group retrieves a paged list of users who belong to the group, or of users with the administrative role for the group.

```json
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
