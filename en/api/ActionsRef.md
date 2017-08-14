---   
title: User Management Actions    
layout: default   
nav_link: User Management Actions   
nav_order: 440    
nav_level: 3    
lang: en    
---   
# User Management Actions

<a name="action" class="api-ref-title">POST /v2/usermanagement/action/{orgId}</a>

Create, update, entitle, and remove users in an organization. The JSON structure allows a maximum of 10 users or [user-groups](glossary.html#usergroup) to be operated on per request.
When a request has been understood and at least partially completed, it returns with HTTP status 200.

This JSON request structure specifies a sequence of commands. Each command entry specifies a user and a sequence of steps to be performed for that user. For a given command entry, steps are performed in the order they appear but the order of execution of commands is not always guaranteed. If the same user is listed in more than one command, results could differ depending on the order of command execution.

## Parameters

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type| Req? |
| :--- | :------ | :---| :--- | --- |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| testOnly | A boolean value indicating whether to run the commands in _test mode_.  If true, parameter syntactic and (limited) semantic checking is done, but the specified operations are not performed, so no user accounts or group memberships are created, changed, or deleted.  The query parameter name is `testOnly` and this parameter is its value. | query | string | false |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Request Body

The JSON request structure specifies a sequence of commands. Each _command_ entry specifies a user or a [user-group](glossary.html#usergroup) and a sequence of _steps_ to be performed for that user/user-group.  

For a given command entry, steps are attempted to be performed in the order that they appear but the order of execution of commands is not always guaranteed. If the same user/user-group is listed in more than one command, results could differ depending on the order of command execution. Use the following order as guidance:
* Creates (addAdobeId, createEnterpriseID, createFederatedID)
* Updates
* Remove entitlements and memberships
* Remove administrative roles
* Add entitlements and memberships
* Add administrative roles
* Remove users from an organization

The following properties are applicable for each _command_ entry. 

__user:__ _string_  
The user field is usually an email address with a UID and domain component `jdoe@example.com`. Organizations can be configured to accept usernames that are not email addresses. In these cases, the `domain` property must be provided in order to identify the user. [Identity Types](glossary.html#identity) explains the different account types available.

__usergroup:__ _string_  
To update the membership lists for a given [user-group](glossary.html#usergroup), specify `add` and `remove` actions in the `do` list for the `usergroup`. Up to 10 memberships can be added/removed in one command entry using the `users` and `productConfiguration` options.

__domain:__ _string_  
Federated IDs that are not email addresses, must supply the domain the user belongs to in order to identify the user. This is required for all operations; create, update, add, remove, and removeFromOrg.  
The domain field must be at the same level as the user field. The domain field is ignored if the user has an Adobe or Enterprise ID. [Identity Types](glossary.html#identity) explains the different account types available.

__requestID:__ _string_  
Arbitrary string which will be returned in the response payload. This is to help assist in identifying the corresponding response to a command entry.

__useAdobeID:__ _boolean_  
When true the user id is interpreted to refer to an existing Type 1 Adobe ID even if a Type 2 or 3 ID exists with the same name.

__do:__  
Lists the series of _steps_ to complete for this command entry. Please note that there can only be __one__ create user operation (createEnterpriseID|createFederatedID|addAdobeID) and __one__ delete user operation (removeFromOrg) in a single command entry.

__addAdobeID:__  
Adds a Type 1 user who has an existing Adobe ID. [Identity Types](glossary.html#identity) explains the different account types available.  
If the organization has not migrated to [OneConsole](glossary.html#oneconsole) then the user will receive an email inviting them to join the organization. The invited user is not available for other operations, such as product access management, until they have accepted the invitation. When you add an Adobe ID user, the command must not include further steps for that user.  
For _migrated_ organizations, the client can include user-information fields such as `firstname` and `lastname`.  
See [user-information](#user-information) for individual field descriptions.
```json
{
  "addAdobeID": {
    "country": "string",
    "email": "string",
    "firstname": "string",
    "lastname": "string",
    "option": "string"
  }
}
```

__createEnterpriseID:__  
Creates a Type 2 (Enterprise) Adobe ID. [Identity Types](glossary.md#identity) explains the different account types available.  
See [user-information](#user-information) for individual field descriptions.
```json
{
  "createEnterpriseID": {
    "country": "string",
    "email": "string",
    "firstname": "string",
    "lastname": "string",
    "option": "string"
  }
}
```

__createFederatedID:__  
Creates a Type 3 (Federated) Adobe ID. [Identity Types](glossary.md#identity) explains the different account types available.  
See [user-information](#user-information) for individual field descriptions.
```json
{
  "createFederatedID": {
    "country": "string",
    "email": "string",
    "firstname": "string",
    "lastname": "string",
    "option": "string"
  }
}
```
__<a name="user-information" class="api-ref-subtitle">User Information Fields</a>__  
* __firstname:__ _string_; Limited to 250 characters. Required for `createEnterpriseID` and `createFederatedID`. Optional for `adobeAdobeID` when a migrated organization.
* __lastname:__ _string_; Limited to 250 characters. Required for `createEnterpriseID` and `createFederatedID`. Optional for `adobeAdobeID` when a migrated organization.
* __email:__ _string_; A valid email address. Required for `createEnterpriseID`, `addAdobeID` and `createFederatedID` and `adobeAdobeID` for migrated organizations.
* __country:__ _string_; A valid ISO 2-character country code for a country in which Adobe does business. Optional for `createEnterpriseID` and `adobeAdobeID` for migrated organizations. Required for `createFederatedID`. The `country` value cannot be updated after it is set.
* __option:__ _string_, possible values: `{ignoreIfAlreadyExists, updateIfAlreadyExists}`; In addition to the new user's field values, the parameters can include an _option_ flag that specifies how to perform the create operation when a user with the given ID already exists in the user database. Default behaviour is `ignoreIfAlreadyExists`. Optional property for `createEnterpriseID`, `createFederatedID`, `addAdobeID`
  - `ignoreIfAlreadyExists`: If the ID already exists, ignore the _create_ step but process any other steps in the command entry for this user.
  - `updateIfAlreadyExists`: If the ID already exists, perform an _update_ action using the parameters in the create step. After updating all fields present in the step, process any other steps in the command entry for this user.

__update:__  
The `update` action writes new personal information to the user's account details. You can update Enterprise and Federated IDs that are managed by your organization.  
Independent Adobe IDs are managed by the individual user and cannot be updated through the User Management API. Attempting to update information for a user who has an Adobe ID will result in error [error.update.adobeid.no](errorRef.html#adobeidno).  
For Federated IDs, the `update` request can only change the information that is stored by Adobe. You cannot change information your organization stores outside of Adobe through the User Management API. You can, however, include a `username` field for users whose email address is in your domain. The `username` value must not include an at-sign character (@). The parameters of an update step specify the changed fields and their new values. If you do not specify a field, its value remains unchanged.  
[Identity Types](glossary.md#identity) explains the different account types available. See [user-information](#user-information) for individual field descriptions.  
```json
{
  "update": {
    "country": "string",
    "email": "string",
    "firstname": "string",
    "lastname": "string",
    "option": "string"
  }
}
```

__add:__
Enables the entitlement or membership of users to product configurations and [user-groups](glossary.md#user-group). Product configurations correspond to specific product access rights, so adding product access for a user is the same as adding that user to the corresponding product configuration.
```json
{
  "add": {
    "productConfiguration": [
      "product_config_name"
    ],
    "user": [
      "string"
    ],
    "usergroup": [
      "usergroup_name"
    ]
  }
}
```

__remove:__
Removes the entitlement or membership of users from product configurations and [user-groups](glossary.md#user-group). Product configurations correspond to specific product access rights, so removing product access for a user is the same as removing that user from the corresponding product configuration.
```json
{
  "remove" : {
    "usergroup" : ["DevOps"]
  }
}
```
Remove the user from all product configurations:
```json
{
  "remove" : "all"
}
```
__product:__
A list of product configurations with a maximum of 10 entries. This can be used with the `user` or `usergroup` root commands and is applicable to the `add` and `remove` operations.

__usergroup:__
A list of user-groups with a maximum of 10 entries. This can be used with the `user` root command and is applicable to the `add` and `remove` operations.

__user:__
A list of users with a maximum of 10 entries. This can be used with the `usergroup` root command and is applicable to the `add` and `remove` operations.

__addRoles:__
Grant administrative privileges to the product configuration or user-group for the specified user.
```json
{
  "addRoles": {
    "admin": [
      "string"
    ],
    "productAdmin": [
      "string"
    ]
  }
}
```

__removeRoles:__
When a user is a member of a product configuration, this command will revoke administrative privileges for that user in that product configuration or user-group.
```json
{
  "removeRoles": {
    "admin": [
      "string"
    ],
    "productAdmin": [
      "string"
    ]
  }
}
```
__productAdmin:__
A list of products with a maximum of 10 entries. This can only be used with the `user` root command and is applicable to the `addRoles` and `removeRoles` operations.

__admin:__
A list of product configurations and user-groups with a maximum of 10 entries. This can only be used with the `user` root command and is applicable to the `addRoles` and `removeRoles` operations. To manage organization administrators use the identifer "org":
```json
{
  "addRoles": {
    "admin": [
      "org"
    ]
  }
}
```

__removeFromOrg:__
Removes the user's membership in the organization, and optionally from membership in a domain that is linked to the given organization through the trusted-domain relationship. There can only be a single `removeFromOrg` action in a command entry. If present, the removal action will be last step invoked.
```json
{
  "removeFromOrg": {
    "deleteAccount": boolean
  }
}
```

__deleteAccount:__ _boolean_
If true then if the account is owned by the organization, the account is also deleted. Note that Adobe IDs are never deleted because they are owned by the user, not the organization. The default value is false.


### Examples

Creates a Type 3 user and adds them to the [product configurations](glossary.md#plc) 'Photoshop' and 'Illustrator' and removes them from the user-group 'devOps'. The user is identified by passing the username and domain.
```json
{
  "user" : "jdoe",
  "domain" : "example.com",
  "requestID" : "ed2149",
  "do" :  [
  {
    "createFederatedID": {
      "email": "john.doe@example.com",
      "country": "US",
      "firstname": "John",
      "lastname": "Doe"
    }
  },
  {
    "add" : {
      "product" : [ "Photoshop", "Illustrator"]
    }
  },
  {
    "remove" : {
      "usergroup" : ["DevOps"]
    }
  }]
}
```
Create a Type 2 user:
```json
{
  "user": "jane.doe@example.com",
  "do": [
    {
      "createEnterpriseID": {
        "email": "jane.doe@example.com",
        "country": "JP",
        "firstname": "Jane",
        "lastname": "Doe"
      }
    }
  ]
}
```
Usergroup as the root command:
```json
{
  "usergroup": "DevOps",
  "do": [
    {
      "add": {
        "product": [
          "Config1_Nickname"
        ],
        "users": [
          "user1@myCompany.com"
        ]
      },
      "remove": {
        "product": [
          "Config2_Nickname"
        ],
        "users": [
          "user2@myCompany.com"
        ]
      }
    }
  ]
}
```
Update a Type 2 user using the update command:
```json
[
  {
    "user": "jdoe@example.com",
    "do": [
      {
        "update": {
          "email": "jdoe@example.com",
          "firstname": "Jane",
          "lastname": "Doe",
          "username": "jdoe"
        }
      }
    ]
  }
]
```
Update a Type 2 user using the createEnterpriseID command and the option flag:
```json
[
  {
    "user": "jdoe@example.com",
    "do": [
      {
        "createEnterpriseID": {
          "email": "jdoe@example.com",
          "firstname": "Jane",
          "lastname": "Doe",
          "username": "jdoe",
          "option": "updateIfAlreadyExists"
        }
      }
    ]
  }
]
```
Removing a user from all their product entitlements:
```json
[
  {
    "user": "jdoe@example.com",
    "do": [
      {
        "remove": "all"
      }
    ]
  }
]
```

### Request Body Schema

```json
[
  {
    "do": [
      {
        "add": {
          "product": [
            "string"
          ],
          "user": [
            "string"
          ],
          "usergroup": [
            "string"
          ]
        },
        "addAdobeID": {
          "country": "string",
          "email": "string",
          "firstname": "string",
          "lastname": "string",
          "option": "string"
        },
        "addRoles": {
          "admin": [
            "string"
          ],
          "productAdmin": [
            "string"
          ]
        },
        "createEnterpriseID": {
          "country": "string",
          "email": "string",
          "firstname": "string",
          "lastname": "string",
          "option": "string"
        },
        "createFederatedID": {
          "country": "string",
          "email": "string",
          "firstname": "string",
          "lastname": "string",
          "option": "string"
        },
        "remove": {},
        "removeFromOrg": {
          "deleteAccount": boolean
        },
        "removeRoles": {
          "admin": [
            "string"
          ],
          "productAdmin": [
            "string"
          ]
        },
        "update": {
          "country": "string",
          "email": "string",
          "firstname": "string",
          "lastname": "string",
          "option": "string"
        }
      }
    ],
    "domain": "string",
    "requestID": "string",
    "useAdobeID": boolean,
    "user": "string",
    "usergroup": "string"
  }
]

```
___

## Responses

__Content-Type:__ _application/json_

### 200 OK
The request was understood and at least partially completed. The response body returns a more complete description of the result in JSON format.
If the result status is:
* __success__: All the actions were completed. `completed` field will equal the total of commands processed.
* __partial__: Some of the actions failed. `completed` and `notCompleted` fields with identify the number of commands that succeeded and failed.
* __error__: All the requested actions failed. `completed` will be 0 and `notCompleted` will show the number of requests that failed.

When the result is partial or error, the errors field lists will include the specific actions that failed with corresponding error information. Warnings can also be returned with details of deprecated commands. Warnings will not cause the command to fail.

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
      "requestID": "Tow 2 Two 2 Two 2 Two 2 !@#$%^&*()_",
      "message": "User Id does not exist: test@test_fake.us",
      "user": "test@test_fake.us",
      "errorCode": "error.user.nonexistent"
    },
    {
      "index": 3,
      "step": 0,
      "requestID": "Four 4 Four 4 Four 4 !@#$%^&*()_",
      "message": "Group NON_EXISTING_GROUP was not found",
      "user": "user4@example.com",
      "errorCode": "error.group.not_found"
    },
    {
      "index": 5,
      "step": 0,
      "requestID": "Six 6 Six 6 Six 6 !@#$%^&*()_",
      "message": "User Id does not exist: test@test_fake.fake",
      "user": "test6@test_fake.fake",
      "errorCode": "error.user.nonexistent"
    },
    {
      "index": 7,
      "step": 0,
      "requestID": "Eight 8Eight 8 Eight 8 !@#$%^&*()_",
      "message": "Changes to users are only allowed in claimed domains.",
      "user": "fake8@faketest.com",
      "errorCode": "error.domain.trust.nonexistent"
    },
    {
      "index": 9,
      "step": 0,
      "requestID": "Ten 10 Ten 10 Ten 10 !@#$%^&*()_",
      "message": "Group NON_EXISTING_GROUP was not found",
      "user": "user10@example.com",
      "errorCode": "error.group.not_found"
    }
  ],
  "result": "partial",
  "warnings": [
    {
      "warningCode": "warning.command.deprecated",
      "requestID": "Four 4 Four 4 Four 4 !@#$%^&*()_",
      "index": 3,
      "step": 0,
      "message": "'product' command is deprecated. Please use productConfiguration.",
      "user": "user4@example.com"
    },
    {
      "warningCode": "warning.command.deprecated",
      "requestID": "Ten 10 Ten 10 Ten 10 !@#$%^&*()_",
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
  "completed" 1,
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
* __errorCode:__ _string_; The error type. See [Errors](ErrorRef.html) for a full list.
* __requestID:__ _string_; A developer-defined ID passed into the request which you can use to match this response to a specific request.
* __user:__ _string_; The user defined in the root of the command entry.

__warnings:__  
An array of warnings. Each warning entry is an object with the attributes below. This section is ommitted if no warnings were generated.

* __index:__ _integer_; The 0-based index of the command entry in the commands structure.
* __step:__ _string_; The 0-based index of the action step within that command entry.
* __message:__ _string_; A description of the warning.
* __warningCode:__ _string_; The warning type. See [Errors](ErrorRef.html) for a full list.
* __requestID:__ _string_; A developer-defined ID passed into the request which you can use to match this response to a specific request.
* __user:__ _string_; The user defined in the root of the command entry.

## Schema Model

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
## Responses with Error Status

If the response has a status other than 200, the request was not processed.  The status code indicates the reason type of error; this section provides some common causes for these errors.

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}