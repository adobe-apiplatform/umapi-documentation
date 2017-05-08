# Manage Pending User Invitations

When you add a user with an Adobe ID to your organization, the user receives an email invitation. The user is not added to your organization until the user clicks the link in the email and accepts the invitation. An invite is pending until the user accepts it, an admin revokes it, or the invite expires.

You can send GET requests to the **{orgId}/invites** resource to retrieve a list of pending invites and to get information about pending invites for a specific user. For details, see [Query Users](queryusers.md)

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

```
{"status": "success"}
```

A failed request can result in a response with one of these HTTP status values:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.
* **404 Not Found** : No pending invites exist for user.
* **500 Internal Server Error** : A server-side error occurred when resending or revoking an invite.

The response body contains the status (an error code) and a status message. For more information about the possible error codes and messages, see [Error Conditions](errorref.md).
