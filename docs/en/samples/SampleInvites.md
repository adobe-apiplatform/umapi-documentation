# Manage Pending User Invites

When you use the **addAdobeID** command to add a user to your organization, the user gets an email invite, and is not added to your list of users until the invite is accepted. The following samples show how to  view and manage pending invites that have been sent, and have not yet been accepted.

## List and Examine Pending Invites

Retrieve a list of pending invites for your organization or for a single user with a GET request to the **invites** resource.

```json
========================= REQUEST ==========================
GET https://usermanagement.adobe.io/v2/usermanagement/{myOrgId}/invites
------------------------- headers --------------------------
Accept: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}

========================= REQUEST ==========================
GET https://usermanagement.adobe.io/v2/usermanagement/{myOrgId}/invites/{email}
------------------------- headers --------------------------
Accept: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

***

## Resend a Pending Invite

Resend an invite for a given email address with a POST request to the **invites** resource.

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/{myOrgId}/invites/{email}
------------------------- headers --------------------------
Accept: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

***

## Revoke a Pending Invite

Revoke a pending invite for a given email address with a DELETE request to the **invites** resource.

```json
========================= REQUEST ==========================
DELETE https://usermanagement.adobe.io/v2/usermanagement/{myOrgId}/invites/{email}
------------------------- headers --------------------------
Accept: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```
