---
layout: default
nav_link: User Management Resource Reference
nav_order: 50
nav_level: 1
lang: en
---

# User Management Resource Reference

Call the user-management API to request changes to your Adobe user accounts.

* You can create new accounts for account types Enterprise ID and Federated ID.
* You can invite users to join your organization with account type Adobe ID. In this case, the user is identified by email and the Adobe ID can already exist or be created after the invitation is issued. You can also resend or revoke pending invites.
* You can update the user information associated with an Enterprise ID or Federated ID account that is managed by your organization.
* You can manage product access and user-group membership for users.
* You can delete accounts from your organization.
* You can initiate password reset for Enterprise ID users.

A management request specifies the users to act upon and the specific actions to take for each user.

## Requests

To request management actions, send a POST request to the **action/orgId** resource, with the specification for the specific actions to take contained in the body of the request.

```clike
POST [UM_Server]/action/{orgId}
```

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".

**HEADERS** : You must include these headers in your request:

* **Authorization** : A current access token obtained from token-exchange request.
* **Content-type** : application/json
* **x-api-key** : The API key assigned to your API client account.

**QUERY PARAMETERS** : Pass the optional query parameter **testOnly=true** if the call is for testing purposes. All checking and processing is done, but no accounts are created, changed, or deleted.

**BODY** : The body of your request must contain the JSON-format **commands** list.

This JSON structure specifies a sequence of commands. Each command entry specifies a user and a sequence of steps to be performed for that user. For a given command entry, steps are performed in the order they appear. The order of execution of commands is not guaranteed. If the same user is listed in more than one command, results could differ depending on the order of command execution.

* For details of the **commands** structure and user management steps, see **[User Management Actions](ActionsRef.md)**
* For examples of different types of management action requests, see the samples in the **[User Management Walkthrough](../samples/index.md)**.

## Responses

When a request has been understood and at least partially completed, it returns with **HTTP status 200**. The response body returns a more complete description of the result in JSON format:

```clike
{ "result": "success|partial|error" ... }
```

If the result is partial (meaning some of the actions failed) or error (meaning all requested actions failed), additional fields show details of which requests failed, and why. See details of the JSON structure below.

A failed request can result in a response with one of these HTTP status values and an error message in the response body:

| Code | Explanation |
| --- | ---- |
| **400 Bad Request** | Some parameters of the request were not understood by the server. |
| **401 Unauthorized** | Invalid or expired token. |
| **429 Too Many Requests** | The server only accepts a certain number of requests per interval, as configured for your organization. This response indicates that you have exceeded this limit. For an example of how to retry a request with exponential back-off, see the [User Management Walkthrough](../samples/index.md). |

### Failed action responses

When the request succeeded but some actions failed, the JSON the response body contains additional fields that show how many of the requested actions completed successfully or failed:

```clike
{ "result": "partial",
  "completed" : 6,
  "notCompleted" : 3,
  "errors" : [...]
```

When "notCompleted" is non-zero, the "errors" field lists the specific actions that failed, with error information:

```clike
"errors" : [
     { "index" : xx, "step" : xx, "requestID" : "xx",
     "user": "uid",
     "message" : "descriptive error message",
     "errorCode" : "code" }, ...
```

In each error entry, the Index and Step identify the failed action by its position in the **commands** structure in the request.

* The "index" value is the 0-based index of the command entry in the **commands** structure.
* The "step" value is the 0-based index of the action step within that command entry.
* The "requestID" value is a developer-defined ID passed into the request, which you can use to match this response to a specific request.

### Response examples

This example shows the result of a request for 9 operations, of which 3 failed:

```clike
{ "result": "partial",
  "completed" : 6,
  "notCompleted" : 3,
  "errors" : [
   { "index" : 3, "step" : 1, "requestID" : "12345",
     "user": "jdoe@example.com",
     "message" : "User in wrong domain",
     "errorCode" : "error.user.belongs_to_another_org" },
   { "index" : 5, "step" : 1, "requestID" : "12336B",
     "user": "u2@example.com",
     "message" : "User does not exist",
     "errorCode" : "error.user.nonexistent" },
   { "index" : 8, "Step" : 1, "RequestID" : "z999",
     "user": "tjones@example.com",
     "message" : "Add to nonexistent group: Photoshop",
     "errorCode" : "error.group.not_found" }
   ] }
```

This example shows a response to a test-only request.

```clike
{ "result": "partial",
  "completed" : 0,
  "notCompleted" : 1,
  "errors" : [
   { "index" : 3, "step" : 1, "requestID" : "12345",
     "user": "jdoe@example.com",
     "message" : "User in wrong domain",
     "errorCode" : "error.user.belongs_to_another_org" }],
  "completedInTestMode" : 8
  }
```

All error codes are constant strings in the format **"error.*.*"**. For more information about the possible error codes and messages, see [Error Conditions](ErrorRef.md).
