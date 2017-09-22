---
layout: default
nav_link: Manage Pending User Invitations
nav_order: 461
nav_level: 3
lang: en
---

# Manage Pending User Invitations

**DEPRECATED:** These APIs have been deprecated. An exact date for removal will be confirmed before the end of 2017 but you should look to update your scripts as soon as possible.

<hr class="api-ref-rule">

When you add a user with an Adobe ID to your organization, the user receives an email invitation. The user is not added to your organization until the user clicks the link in the email and accepts the invitation. An invite is pending until the user accepts it, an admin revokes it, or the invite expires.

You can send GET requests to the **{orgId}/invites** resource to retrieve a [list of pending invites](#pending) and to get information about [pending invites for a specific user](#user).

You can send POST and DELETE requests to the **{orgId}/invites** resource to resend or revoke a pending invite for a specific user, identified by their Adobe ID email.

* Resend pending user invites:

```
POST [UM_Server]/{orgId}/invites/{email}
```
* Revoke pending user invites:

```
DELETE [UM_Server]/{orgId}/invites/{email}
```

### Responses

A successful request returns a response with **HTTP status 200**. The response body for a successful POST or DELETE request contains the status in JSON format.

```json
{"status": "success"}
```

A failed request can result in a response with one of these HTTP status values:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.
* **404 Not Found** : No pending invites exist for user.
* **500 Internal Server Error** : A server-side error occurred when resending or revoking an invite.

The response body contains the status (an error code) and a status message. For more information about the possible error codes and messages, see [Error Conditions](ErrorRef).

## <a name="pending" class="api-ref-subtitle">List Pending User Invites</a>

A GET request to the **invites** resource retrieves a paged list of pending invitations for invited users. The number of invites returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list. All query parameters are optional.

```
GET [UM_Server]/{orgId}/invites/[?page={n}&includeExpired=true|false&sortColumn=EMAIL|LAST_SENT_DTS&sortOrder=ASC|DESC]
```

* **{orgId}** : Required. The unique ID of your organization.
* **page** : A zero-based index for the start entry of the paged response. Default is 0.
* **includeExpired** : When true, pending invites that have expired are included. Default is true.
* **sortColumn** : The column or field to use for sorting the result list. One of EMAIL (alphabetical by email address) or LAST_SENT_DTS (the date-time stamp of the most recently sent invite). Default is LAST_SENT_DTS.
* **sortOrder** : Sort order of the result list. One of ASC (ascending date or alpha order) or DESC (descending date or alpha order). Default is DESC.

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user data in JSON format:

```json
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

## <a name="user" class="api-ref-subtitle">Query Individual Pending User</a>

A GET request to the individual email of an invited user retrieves information about invitations for that user. You can choose whether to include expired invites. Users are identified by their unique ID, which is the complete email address. The body of the response contains the invite information in JSON format.

```
GET [UM_Server]/organizations/{orgId}/invites/{email}[?includeExpired=true|false&sortColumn=EMAIL|LAST_SENT_DTS&sortOrder=ASC|DESC]
```

* **{orgId}** : Required. Your organization ID.
* **{email}** : Required. The unique user ID. The full Adobe ID email address.
* **includeExpired** : When true, include expired invites. Default is true.
* **sortColumn** : The column or field to use for sorting the result list. One of EMAIL (alphabetical by email address) or LAST_SENT_DTS (the date-time stamp of the most recently sent invite). Default is LAST_SENT_DTS.
* **sortOrder** : Sort order of the result list. One of ASC (ascending date or alpha order) or DESC (descending date or alpha order). Default is DESC.

### Responses

A successful request returns the requested data with **HTTP status 200**. The response body contains the requested user data in JSON format. Invite data includes the invitation ID and information about who sent the invitation. For example:

```json
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
