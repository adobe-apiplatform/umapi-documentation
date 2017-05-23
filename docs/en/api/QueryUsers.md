---
layout: default
nav_link: List and Query Users
nav_order: 510
nav_level: 3
lang: en
---

# List and Query Users

User information defined for your organization is available through the **{orgId}/users**. You can also get member lists through the user-group and product-configuration resources.

* Retrieve a paged list of all users for your organization, or members of a User Group:

```
GET [UM_Server]/{orgId}/users[?page={n}&domain={trusted_domain_name}]
GET [UM_Server]/{orgId}/users/{page}/{groupName}
```
* Retrieve a paged list of all pending invites users who have been invited to join your organization:

```
GET [UM_Server]/{orgId}/invites[?page={n}]
```
* Access information for individual existing users or pending users by their email address.

```
GET [UM_Server]/{orgId}/users/{email}
GET [UM_Server]/{orgId}/invites/{email}
```

NOTE: For compatability with previous releases, user information can also be accessed through the **users/{orgId}** or **organizations/{orgId}/users** resources.

***

## List Existing Users

A GET request to the **users** resource retrieves a paged list of existing users in your organization.The number of users returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list.

```json
GET [UM_Server]/{orgId}/users/[?page={n}&domain={trusted_domain_name}]
GET [UM_Server]/users/{orgId}/{page}[?domain={trusted_domain_name}]
```

* **{orgId}** : Required. The unique ID of your organization.
* **{page}** : A zero-based index for the start entry of the paged response. Where provided as an optional query parameter, default is 0.
* **domain={trusted_domain_name}** : Optional query parameter retrieves users from a domain linked to an organization in the Trusted Domain relationship.

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user data in JSON format:

```
{
  "result": "success",
  "users" : [ { user1 }, ... ]
  "lastPage" : true
}
```

A failed request can result in a response with one of these HTTP status values, with an error message in the response body:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.

_Note that server errors can occur that require exponential back-off on retry._

***

## List Pending User Invites

A GET request to the **invites** resource retrieves a paged list of pending invitations for invited users. The number of invites returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list. All query parameters are optional.

```json
GET [UM_Server]/{orgId}/invites/[?page={n}&includeExpired=true|false&sortColumn=EMAIL|LAST_SENT_DTS&sortOrder=ASC|DESC]
```

* **{orgId}** : Required. The unique ID of your organization.
* **page** : A zero-based index for the start entry of the paged response. Default is 0.
* **includeExpired** : When true, pending invites that have expired are included. Default is true.
* **sortColumn** : The column or field to use for sorting the result list. One of EMAIL (alphabetical by email address) or LAST_SENT_DTS (the date-time stamp of the most recently sent invite). Default is LAST_SENT_DTS.
* **sortOrder** : Sort order of the result list. One of ASC (ascending date or alpha order) or DESC (descending date or alpha order). Default is DESC.

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user data in JSON format:

```
[
  {
    "email": "invitee@example.com",
    "inviteCode": "91UYX8HKTQYU299QPJ8SKV4",
    "lastSentDTS": 1471648979000,
    "invitedBy": {
      "id": "B476578AC50DDEDD1A4719B@AdobeID",
      "email": "JohnDoe@mydomain.com",
      "firstName": "John",
      "lastName": "Doe",
      "countryCode": "US"
    }
  },
  ...
]
```

A failed request can result in a response with one of these HTTP status values, with an error message in the response body:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.
* **404 Not Found** : No pending invites exist for the organization.
* **500 Internal Server Error**

_Note that server errors can occur that require exponential back-off on retry._

***

## Query Individual Existing User

A GET request to the individual user under the **users** resource for your organization retrieves information for that user. Users are identified by their unique ID, which is the Adobe email address or, for Federated IDs, the username. The body of the response contains the user information in JSON format. For Federated ID, the user information includes the username and domain name.

```json
GET [UM_Server]/organizations/{orgId}/users/{email}
GET [UM_Server]/users/{orgId}/{email}
```

* **{orgId}** : Required. Your organization ID.
* **{email}** : Required. The unique user ID. The full email address (for Adobe ID or Enterprise ID) or the username portion of the email address (for Federated ID).

### Responses

A successful request returns the requested data with **HTTP status 200**. The response body contains the requested user data in JSON format.

This example shows a response for

```json
GET [UM_Server]/organizations/{orgId}/users/{email}
```

with all fields present. Fields can be missing if values were never supplied or are not applicable for an account type.

```json
{
  "result": "success",
  "user": {
    "email": "JaneDoe@example.com",
    "lastname": "Doe",
    "firstname": "Jane",
    "country": "US",
    "status": "active",
    "type": "federatedID",
    "username": "JaneDoe",
    "domain": "example.com",
    "groups": [
      "Creative Cloud 1",
      "Document Cloud 1",
      "Marketing Cloud 1 - Excel License Users:Analytics",
      "Marketing Cloud 1 - All Report Access:Analytics",
      "Marketing Cloud 1 - Default Access:Audience Manager"
    ],
    "adminRoles": [
      "org",
      "deployment",
      "Document Cloud 1",
      "Creative Cloud 1",
      "Marketing Cloud 1 - Default Access:Audience Manager",
      "Marketing Cloud 1 - Mobile App Admin:Analytics",
      "Marketing Cloud 1 - Excel License Users:Analytics",
      "Marketing Cloud 1 - All Report Access:Analytics"
    ]
  }
}
```

***

## Query Individual Pending User

A GET request to the individual email of an invited user retrieves information about invitations for that user. You can choose whether to include expired invites. Users are identified by their unique ID, which is the complete email address. The body of the response contains the invite information in JSON format.

```json
GET [UM_Server]/organizations/{orgId}/invites/{email}[?includeExpired=true|false&sortColumn=EMAIL|LAST_SENT_DTS&sortOrder=ASC|DESC]
```

* **{orgId}** : Required. Your organization ID.
* **{email}** : Required. The unique user ID. The full Adobe ID email address.
* **includeExpired** : When true, include expired invites. Default is true.
* **sortColumn** : The column or field to use for sorting the result list. One of EMAIL (alphabetical by email address) or LAST_SENT_DTS (the date-time stamp of the most recently sent invite). Default is LAST_SENT_DTS.
* **sortOrder** : Sort order of the result list. One of ASC (ascending date or alpha order) or DESC (descending date or alpha order). Default is DESC.

### Responses

A successful request returns the requested data with **HTTP status 200**. The response body contains the requested user data in JSON format. Invite data includes the invitation ID and information about who sent the invitation. For example:

```
[
  {
    "email": "invitee@example.com",
    "inviteCode": "91UYX8HKTQYU299QPJ8SKV4",
    "lastSentDTS": 1471648979000,
    "invitedBy": {
      "id": "B476578AC50DDEDD1A4719B@AdobeID",
      "email": "JohnDoe@mydomain.com",
      "firstName": "John",
      "lastName": "Doe",
      "countryCode": "US"
    }
  },
]
```

A failed request can result in a response with one of these HTTP status values, with an error message in the response body:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.
* **404 Not Found** : No pending invites exist for the user.
* **500 Internal Server Error** 
