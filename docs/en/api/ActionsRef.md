---   
title: User Management Action Requests    
layout: default   
nav_link: User Management Action API  
nav_order: 400    
nav_level: 2    
lang: en    
---   

# User Management Action API

Use an HTTPS **POST** request to the `action` resource for your organization to request most user-management actions.
```
https://usermanagement.adobe.io/v2/usermanagement/action/{orgId}
```

The body of this request contains a JSON _commands_ structure that you use to specify which actions to perform for which user or user group. You can create, update, entitle, and remove users or user groups in an organization.

When a request has been understood and at least partially completed, it returns with HTTP status 200.

__Throttle Limits__: Maximum 10 requests per minute per a client. See [Throttling Limits](#actionThrottle) for full details.

* [Parameters](#parameters)
* [Request Body](#actionRequestBody)
* [Responses](#responses)
* [Throttling Limits](#actionThrottle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Req? | Description |
| :--- | :---| :---: | :---------- |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| testOnly | query | false | A boolean value indicating whether to run the commands in _test mode_.  If true, parameter syntactic and (limited) semantic checking is done, but the specified operations are not performed, so no user accounts or group memberships are created, changed, or deleted. |
| X-Api-Key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| Content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
| request | body | true | JSON payload containing a series of commands. See [Request Body](#actionRequestBody). |
{:.bordertablestyle}

*****
### <a name="testOnly" class="api-ref-subtitle">Using Test Mode</a>

Supply the **testOnly** parameter in the POST request to the Action API in order to test the behavior of the command set.

```

POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgID}?testOnly=true
-------------------------- body ----------------------------
JSON commands
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

When you set the **testOnly** flag in an action call, the user-management service checks all commands for validity but does not make any actual changes in your user data. Use the flag to make sure that you are passing proper values without risk to the integrity of your user data. The response to a test-mode request reports that 0 operations were "completed". The "completedInTestMode" field reports the number of commands expected to complete without error, subject to limitations.

```
{ "result": "partial",
  "completed" : 0,
  "completedInTestMode" : 3,
  "notCompleted" : 1,
  "errors" : [...]
```

#### Limitations of Test Mode

In normal operation, a command would create a user and then take actions on that user. When you create a user in test mode, the creation operation is not executed. All subsequent actions on that user should then fail. In order to make the test mode useful, it marks as successful any operation that refers to a non-existent user but is otherwise valid.

The test behavior generally reflects the normal behavior of a command set, but the need to ignore the non-existent user leads to limitations of the test that you should be aware of. Some sequences of commands that succeed in test mode do not succeed in normal operation. For example, two attempts to create the same users passes test mode, but is otherwise an error.

#### Test Behavior Cases

The following table shows the behavior of test mode for particular test cases.

| Command Types | Test Behavior |
| --- | --- |
| Create user | Reports errors in command syntax, organization or user type mismatches, conflicting users.Does not create user. |
| Update user info | Reports syntax or field errors. Checks user validity, except non-existent user.Does not make any changes to an existing user or report an error for non-existent user. |
| Add or remove product access | Checks validity of product profile names. Reports error in syntax and limits.Does not make any membership changes for an existing user or report an error for non-existent user. |
| Remove user | Reports errors in command syntax, organization mismatches.Does not remove an existing user or report an error for non-existent user. |
| Reset password | Reports errors in command syntax, organization and user mismatches.Does not send password email or disable the user account. |


## <a name="actionRequestBody" class="api-ref-subtitle">Request Body</a>

The JSON _commands_ structure contained in your POST request specifies a sequence of commands. Each command entry specifies a user or user-group, and a sequence of _steps_ to be performed for that user or user-group.

* The JSON commands structure allows a maximum of 10 users or user groups to be operated on per request.
* For a detailed description of the command structure and syntax, and details of all action steps that can be performed, see [User Action Commands](ActionsCmds.md).

******
## <a name="responses" class="api-ref-subtitle">Responses</a>

- [200: OK](#200)
- [400: Bad Request](#400)
- [401: Unauthorized](#401)
- [403: Forbidden](#403)
- [429: Too Many Requests](#actionThrottle)

__Content-Type:__ _application/json_

### <a name="200" class="api-ref-subtitle">200 OK</a>
The request was understood and at least partially completed. The response body returns a more complete description of the result in JSON format.
If the result status is:
* __success__: All the actions were completed. `completed` field will equal the total of commands processed.
* __partial__: Some of the actions failed. `completed` and `notCompleted` fields with identify the number of commands that succeeded and failed.
* __error__: All the requested actions failed. `completed` will be 0 and `notCompleted` will show the number of requests that failed.

When the result is partial or error, the errors field lists will include the specific actions that failed with corresponding error information. Warnings can also be returned with details of deprecated commands. Warnings will not cause the command to fail.

When using the [testOnly](#testOnly) parameter, the field `completedInTestMode` will be populated with the number of successful commands processed. In this scenario the `completed` field will be 0 as no commands will have been fully processed.

#### Examples
Error status:
```json
{
  "completed": 0,
  "notCompleted": 1,
  "completedInTestMode": 0,
  "errors": [
    {
      "index": 0,
      "step": 0,
      "message": "String too long in command for field: country, max length 2",
      "errorCode": "error.command.string.too_long"
    }
  ],
  "result": "error"
}
```
Partial status:
```json
{
  "completed": 5,
  "notCompleted": 5,
  "completedInTestMode": 0,
  "errors": [
    {
      "index": 1,
      "step": 0,
      "requestID": "Two2_123456",
      "message": "User Id does not exist: test@test_fake.us",
      "user": "test@test_fake.us",
      "errorCode": "error.user.nonexistent"
    },
    {
      "index": 3,
      "step": 0,
      "requestID": "Four4_123456",
      "message": "Group NON_EXISTING_GROUP was not found",
      "user": "user4@example.com",
      "errorCode": "error.group.not_found"
    },
    {
      "index": 5,
      "step": 0,
      "requestID": "Six6_123456",
      "message": "User Id does not exist: test@test_fake.fake",
      "user": "test6@test_fake.fake",
      "errorCode": "error.user.nonexistent"
    },
    {
      "index": 7,
      "step": 0,
      "requestID": "Eight8_123456",
      "message": "Changes to users are only allowed in claimed domains.",
      "user": "fake8@faketest.com",
      "errorCode": "error.domain.trust.nonexistent"
    },
    {
      "index": 9,
      "step": 0,
      "requestID": "Ten10_123456",
      "message": "Group NON_EXISTING_GROUP was not found",
      "user": "user10@example.com",
      "errorCode": "error.group.not_found"
    }
  ],
  "result": "partial",
  "warnings": [
    {
      "warningCode": "warning.command.deprecated",
      "requestID": "Four4_123456",
      "index": 3,
      "step": 0,
      "message": "'product' command is deprecated. Please use productConfiguration.",
      "user": "user4@example.com"
    },
    {
      "warningCode": "warning.command.deprecated",
      "requestID": "Ten10_123456",
      "index": 9,
      "step": 0,
      "message": "'product' command is deprecated. Please use productConfiguration.",
      "user": "user10@example.com"
    }
  ]
}
```
Success status:
```json
{
  "completed": 1,
  "notCompleted": 0,
  "completedInTestMode": 0,
  "result": "success"
}
```

#### Schema Properties

__message:__ _string_  
Only returned if initial validation of the request fails. It is not populated when a 200 status is returned.

```json
{
  "result": "error.organization.invalid_id",
  "message": "Bad organization Id"
}
```

__result:__ _string_, possible values: `{ "success", "error", "partial", "error.apikey.invalid", "error.command.malformed", "error.organization.invalid", "error.organization.migrating" }`  
The status of the request. This property can be used to manage error handling as the value will either be `success` or a corresponding error. If the result status is:
* __success__: All the actions were completed. `completed` field will equal the total of commands processed.
* __partial__: Some of the actions failed. `completed` and `notCompleted` fields with identify the number of commands that succeeded and failed.
* __error__: All the requested actions failed. `completed` will be 0 and `notCompleted` will show the number of requests that failed.

__completed:__ _integer_  
The number of user commands that were successful.

__notCompleted:__ _integer_  
The number of user commands that were unsuccessful. When non-zero the errors field lists the specific actions that failed, with error information.

__completedInTestMode:__ _integer_  
The number of users that were completed in testOnly mode.

__errors:__  
An array of errors. Each error entry is an object with the attributes below. This section is ommitted if no errors were generated.

* __index:__ _integer_; The 0-based index of the command entry in the commands structure.
* __step:__ _string_; The 0-based index of the action step within that command entry.
* __message:__ _string_; A description of the error.
* __errorCode:__ _string_; The error type. See [Errors](ErrorRef.md) for a full list.
* __requestID:__ _string_; A developer-defined ID passed into the request which you can use to match this response to a specific request.
* __user:__ _string_; The user defined in the root of the command entry.

__warnings:__  
An array of warnings. Each warning entry is an object with the attributes below. This section is ommitted if no warnings were generated.

* __index:__ _integer_; The 0-based index of the command entry in the commands structure.
* __step:__ _string_; The 0-based index of the action step within that command entry.
* __message:__ _string_; A description of the warning.
* __warningCode:__ _string_; The warning type. See [Errors](ErrorRef.md) for a full list.
* __requestID:__ _string_; A developer-defined ID passed into the request which you can use to match this response to a specific request.
* __user:__ _string_; The user defined in the root of the command entry.

#### Schema Model

```json
{
  "completed": 0,
  "completedInTestMode": 0,
  "errors": [
    {
      "errorCode": "string",
      "index": 0,
      "message": "string",
      "requestID": "string",
      "step": 0,
      "user": "string"
    }
  ],
  "message": "string",
  "notCompleted": 0,
  "result": "string",
  "warnings": [
    {
      "index": 0,
      "message": "string",
      "requestID": "string",
      "step": 0,
      "user": "string",
      "warningCode": "string"
    }
  ]
}
```
### Responses with Error Status

If the response has a status other than 200, the request was not processed.  The status code indicates the reason type of error; this section provides some common causes for these errors.

{% include_relative partials/badRequest.md anchor="400" %}

{% include_relative partials/unauthorized.md anchor="401" %}

{% include_relative partials/forbidden.md anchor="403" %}

## <a name="actionThrottle" class="api-ref-subtitle">Throttling Limits</a>

{% include_relative partials/throttling.md client=10 global=100 %}
