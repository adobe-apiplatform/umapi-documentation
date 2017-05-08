# Testing Behavior

During development of user-management applications, you can pass the **testOnly** parameter in the URL of a user-management POST request, in order to test the behavior of the command set.

```json

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

```json
{ "result": "partial",
  "completed" : 0,
  "completedInTestMode" : 3,
  "notCompleted" : 1,
  "errors" : [...]
```

## Limitations of Test Mode

In normal operation, a command would create a user and then take actions on that user. When you create a user in test mode, the creation operation is not executed. All subsequent actions on that user should then fail. In order to make the test mode useful, it marks as successful any operation that refers to a non-existent user but is otherwise valid.

The test behavior generally reflects the normal behavior of a command set, but the need to ignore the non-existent user leads to limitations of the test that you should be aware of. Some sequences of commands that succeed in test mode do not succeed in normal operation. For example, two attempts to create the same users passes test mode, but is otherwise an error.

## Test Behavior Cases

The following table shows the behavior of test mode for particular test cases.

| Command Types | Test Behavior |
| --- | --- |
| Create user | Reports errors in command syntax, organization or user type mismatches, conflicting users.Does not create user. |
| Update user info | Reports syntax or field errors. Checks user validity, except non-existent user.Does not make any changes to an existing user or report an error for non-existent user. |
| Add or remove product access | Checks validity of product configuration names. Reports error in syntax and limits.Does not make any membership changes for an existing user or report an error for non-existent user. |
| Remove user | Reports errors in command syntax, organization mismatches.Does not remove an existing user or report an error for non-existent user. |
| Reset password | Reports errors in command syntax, organization and user mismatches.Does not send password email or disable the user account. |
