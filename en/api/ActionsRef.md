---   
title: User Management Actions    
layout: default   
nav_link: User Management Actions   
nav_order: 420    
nav_level: 2    
lang: en    
---   
# User Management Actions

```
POST /v2/usermanagement/action/{orgId}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Request Body](#actionRequestBody)
  - [Schema](#actionRequestBodySchema)
  - [Examples](#actionRequestBodyExamples)
* [Throttling Limits](#getUsersRESTThrottle)

<a name="intro" class="api-ref-subtitle"></a>
Create, update, entitle, and remove users or [user-groups](glossary.html#usergroup) in an organization. The JSON structure allows a maximum of 10 users or user-groups to be operated on per request.
When a request has been understood and at least partially completed, it returns with HTTP status 200.

This JSON request structure specifies a sequence of commands. Each command entry specifies a user (or usergroup) and a sequence of steps to be performed for that user/user-group. For a given command entry, steps are performed in the order they appear but the order of execution of commands is **not** always guaranteed. If the same user/user-group is listed in more than one command, results could differ depending on the order of command execution.

__Throttle Limits__: Maximum 10 requests per minute per a client. See [Throttling Limits](#actionThrottle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Req? | Description |
| :--- | :---| :---: | :---------- |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| <a name="testOnly" class="api-ref-subtitle">testOnly</a> | query | false | A boolean value indicating whether to run the commands in _test mode_.  If true, parameter syntactic and (limited) semantic checking is done, but the specified operations are not performed, so no user accounts or group memberships are created, changed, or deleted. |
| X-Api-Key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| Content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
| request | body | true | JSON payload containing a series of commands. See [Request Body](#actionRequestBody) section for full details. |
{:.bordertablestyle}

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

{% include apiRef/badRequest.md anchor="400" %}

{% include apiRef/unauthorized.md anchor="401" %}

{% include apiRef/forbidden.md anchor="403" %}

## <a name="actionRequestBody" class="api-ref-subtitle">Request Body</a>

The JSON request structure specifies a sequence of commands. Each _command_ entry specifies a user or a [user-group](glossary.html#usergroup) and a sequence of _steps_ to be performed for that user/user-group.  

For a given command entry, steps are attempted to be performed in the order that they appear but the order of execution of commands is not always guaranteed. If the same user/user-group is listed in more than one command, results could differ depending on the order of command execution. Use the following order as guidance:
* Creates ([addAdobeId](#addAdobeID), [createEnterpriseID](#createEnterpriseID), [createFederatedID](#createFederatedID)).
* [Updates](#update) of users' information.
* [Removal](#remove) of entitlements and memberships.
* [Removal](#removeRoles) of administrative roles
* [Adding](#add) of entitlements and memberships
* [Adding](#addRoles) of administrative roles
* [Removal](#removeFromOrg) of users from an organization

### <a name="actionRequestBodyProperties" class="api-ref-subtitle">Properties</a>

The following properties are available for each _command_ entry:

<a name="userRootCommand" class="api-ref-subtitle">__user:__</a> _string_  
The user field is usually an email address with a UID and domain component `jdoe@example.com`. Organizations can be configured to accept usernames that are not email addresses. In these cases, the `domain` property must be provided in order to identify the user. [Identity Types](glossary.html#identity) explains the different account types available.

__usergroup:__ _string_  
To update the membership lists for a given [user-group](glossary.html#usergroup), specify `add` and `remove` actions in the `do` list for the `usergroup`. Up to 10 memberships can be added/removed in one command entry using the `user` and `group` options.

__domain:__ _string_ (_only available with the [user root command](#userRootCommand)_)  
[Federated IDs](glossary.html#federatedId) that are not email addresses, must supply the domain the user belongs to in order to identify the user. This is required for all operations; create, update, add, remove, and removeFromOrg.  
The domain field must be at the same level as the user field. The domain field is ignored if the user has an [Adobe](glossary.html#adobeId) or [Enterprise](glossary.html#enterpriseId) ID. [Identity Types](glossary.html#identity) explains the different account types available.

__requestID:__ _string_  
Arbitrary string which will be returned in the response payload. This is to help assist in identifying the corresponding response to a command entry.

__useAdobeID:__ _boolean_ (_only available with the [user root command](#userRootCommand)_)  
When true the user id is interpreted to refer to an existing [Adobe ID](glossary.html#adobeId) even if a [Enterprise](glossary.html#enterpriseId) or [Federated ID](glossary.html#federatedId) exists with the same name.

__do:__  
Lists the series of _steps_ to complete for this command entry. Please note when using the [user root command](#userRootCommand)) that there can only be __one__ create user operation ([createEnterpriseID](#createEnterpriseID), [createFederatedID](#createFederatedID) or [addAdobeID](#addAdobeID)) and __one__ delete user operation ([removeFromOrg](#removeFromOrg)) in a single command entry.

<a name="addAdobeID" class="api-ref-subtitle">__addAdobeID:__</a> (_only available with the [user root command](#userRootCommand)_)  
Adds a user who has an existing [Adobe ID](glossary.html#adobeId).  The client can include user-information fields such as `firstname` and `lastname`.  
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

<a name="createEnterpriseID" class="api-ref-subtitle">__createEnterpriseID:__</a> (_only available with the [user root command](#userRootCommand)_)  
Creates an [Enterprise ID](glossary.html#enterpriseId). See [user-information](#user-information) for individual field descriptions.
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

<a name="createFederatedID" class="api-ref-subtitle">__createFederatedID:__</a> (_only available with the [user root command](#userRootCommand)_)  
Creates a [Federated ID](glossary.html#federatedId). See [user-information](#user-information) for individual field descriptions.
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
<a name="user-information" class="api-ref-subtitle">__User Information Fields__</a>  
* __firstname:__ _string_; Limited to 250 characters. Required for `createEnterpriseID` and `createFederatedID`. Optional for `addAdobeID` when a _[migrated](glossary.html#oneconsole)_ organization otherwise it is ignored for [Adobe IDs](glossary.html#adobeId).
* __lastname:__ _string_; Limited to 250 characters. Required for `createEnterpriseID` and `createFederatedID`. Optional for `addAdobeID` when a _[migrated](glossary.html#oneconsole)_ organization otherwise it is ignored for [Adobe IDs](glossary.html#adobeId).
* __email:__ _string_; A valid email address. Required for `createEnterpriseID`, `addAdobeID` and `createFederatedID`.
* __country:__ _string_; A valid ISO 2-character country code. Optional for `createEnterpriseID` and `addAdobeID` for _[migrated](glossary.html#oneconsole)_ organizations. Required for `createFederatedID`. The `country` value cannot be updated after it is set.
* __option:__ _string_, possible values: `{ignoreIfAlreadyExists, updateIfAlreadyExists}`; In addition to the new user's field values, the parameters can include an _option_ flag that specifies how to perform the create operation when a user with the given ID already exists in the user database. Default behaviour is `ignoreIfAlreadyExists`. Optional property for `createEnterpriseID`, `createFederatedID`, `addAdobeID`.
  - `ignoreIfAlreadyExists`: If the ID already exists, ignore the _create_ step but process any other steps in the command entry for this user.
  - `updateIfAlreadyExists`: If the ID already exists, perform an _update_ action using the parameters in the create step. After updating all fields present in the step, process any other steps in the command entry for this user.

<a name="update" class="api-ref-subtitle">__update:__</a> (_only available with the [user root command](#userRootCommand)_)  
The `update` action writes new personal information to the user's account details. You can update [Enterprise](glossary.html#enterpriseId) and [Federated IDs](glossary.html#federatedId) that are managed by your organization.  
Independent [Adobe IDs](glossary.html#adobeId) are managed by the individual user and cannot be updated through the User Management API. Attempting to update information for a user who has an [Adobe ID](glossary.html#adobeId) will result in error [error.update.adobeid.no](errorRef.html#adobeidno).  
For [Federated IDs](glossary.html#federatedId), the `update` request can only change the information that is stored by Adobe. You cannot change information your organization stores outside of Adobe through the User Management API. You can, however, include a `username` field for users whose email address is in your domain. The `username` value must not include an at-sign character (@). The parameters of an update step specify the changed fields and their new values. If you do not specify a field, its value remains unchanged.  
[Identity Types](glossary.html#identity) explains the different account types available. See [user-information](#user-information) for individual field descriptions.  
```json
{
  "update": {
    "country": "string",
    "email": "string",
    "firstname": "string",
    "lastname": "string",
    "option": "[ignoreIfAlreadyExists|updateIfAlreadyExists]"
  }
}
```

<a name="add" class="api-ref-subtitle">__add:__</a>  
Enables the entitlement or membership of users to product profiles and [user-groups](glossary.html#user-group). {% include apiRef/plc.md plural=true capitalize=true %} correspond to specific product access rights, so adding product access for a user is the same as adding that user to the corresponding {% include apiRef/plc.md %}. You can add a maximum of 10 memberships in one command entry. See [Add attributes](#addRemoveAttr) section for full details of the following attributes:
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

<a name="remove" class="api-ref-subtitle">__remove:__</a>  
Removes the entitlement or membership of users from {% include apiRef/plc.md %}s and [user-groups](glossary.html#user-group). {% include apiRef/plc.md plural=true %} correspond to specific product access rights, so removing product access for a user is the same as removing that user from the corresponding {% include apiRef/plc.md %}. You can remove a maximum of 10 memberships in one command entry, unless you use the special “all” parameter to remove all memberships for the user or user-group. See [Remove attributes](#addRemoveAttr) section for full details of the following attributes:
```json
{
  "remove" : {
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
Additionally you can pass the attribute `all` to remove the user from all groups including {% include apiRef/plc.md %} and user-groups:
```json
{
  "remove" : "all"
}
```
<a name="addRemoveAttr" class="api-ref-subtitle">__Add/Remove Attributes__</a>
* __group:__; A list of {% include apiRef/plc.md %} with a maximum of 10 entries. This can be used with the `user` or `usergroup` root commands and is available in the [add](#add) and [remove](#remove) operations.

* __usergroup:__ (_only available with the [user root command](#userRootCommand)_); A list of user-groups with a maximum of 10 entries. This can be used with the `user` root command and is available in the [add](#add) and [remove](#remove) operations.

* __user:__ (_only available with the [user-group root command](#usergroupRootCommand)_); A list of users with a maximum of 10 entries. This can be used with the `usergroup` root command and is applicable to the [add](#add) and [remove](#remove) operations.

<a name="addRoles" class="api-ref-subtitle">__addRoles:__</a> (_only available with the [user root command](#userRootCommand)_)  
Grant administrative privileges to the {% include apiRef/plc.md %} or user-group for the specified user. See [Add Role attributes](#addRemoveRoleAttr) section for full details of the following attributes:
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

<a name="removeRoles" class="api-ref-subtitle">__removeRoles:__</a> (_only available with the [user root command](#userRootCommand)_)  
When a user is a member of a {% include apiRef/plc.md %}, this command will revoke administrative privileges for that user in that {% include apiRef/plc.md %} or user-group. See [Remove Role attributes](#addRemoveRoleAttr) section for full details of the following attributes:
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
<a name="addRemoveRoleAttr" class="api-ref-subtitle">__Add/Remove Role Attributes__</a>  
* __productAdmin:__ (_only available with the [user root command](#userRootCommand)_); A list of products (with a maximum of 10 entries) to assign the user as a [Product Administrator](glossary.html#productAdmin). This can only be used with the `user` root command and is applicable to the `addRoles` and `removeRoles` operations. 

* __admin:__ (_only available with the [user root command](#userRootCommand)_); A list of product profiles and user-groups (with a maximum of 10 entries) to assign the user as an Administrator. This can only be used with the `user` root command and is applicable to the `addRoles` and `removeRoles` operations. Possible roles include:
  * "org": Assign the user as a [System Administrator](glossary.html#orgAdmin).
  * "deployment": Assign the user as a [Deployment Administrator](glossary.html#deployment).
<!--  * "support": Assign the user as a [Support Administator](glossary.html#supportAdmin). -->
  * "{product-profile-name}": Assign user as a [{% include apiRef/plc.md capitalize=true %} Administrator](glossary.html#productProfileAdmin).
  * "{user-group-name}": Assign user as a [UserGroup Administrator](glossary.html#usergroupAdmin). 
```json
  {
      "addRoles": {
        "admin": [
          "org"
        ]
      }
  }
```

<a name="removeFromOrg" class="api-ref-subtitle">__removeFromOrg:__</a> (_only available with the [user root command](#userRootCommand)_)  
Removes the user's membership in the organization, and optionally from membership in a domain that is linked to the given organization through the trusted-domain relationship. This includes any product profiles and user-groups in the organization that they are a member of. There can only be a single `removeFromOrg` action in a command entry. If present, the removal action will be the last step invoked. If the user is specified by email address, then the domain of the email address specifies the domain of the account. If the user is specified by Username, the domain must be provided.
```json
{
  "removeFromOrg": {
    "deleteAccount": boolean
  }
}
```

* __deleteAccount:__ _boolean_; If true then if the account is owned by the organization, the account is also deleted. Note that [Adobe IDs](glossary.html#adobeId) are never deleted because they are owned by the user, not the organization. The default value is false.

### <a name="actionRequestBodyExamples" class="api-ref-subtitle">Examples</a>

Creates a [Federated ID](glossary.html#federatedId) and adds them to the [{% include apiRef/plc.md plural=true %}](glossary.html#plc) 'Photoshop' and 'Illustrator' and removes them from the user-group 'devOps'. The user is identified by passing the username and domain.
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
      "productConfiguration" : [ "Photoshop", "Illustrator"]
    }
  },
  {
    "remove" : {
      "usergroup" : ["Photoshop"]
    }
  }]
}
```
Create an [Enterprise ID](glossary.html#enterpriseId):
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
        "productConfiguration": [
          "Config1_Nickname"
        ],
        "user": [
          "user1@myCompany.com"
        ]
      },
      "remove": {
        "productConfiguration": [
          "Config2_Nickname"
        ],
        "user": [
          "user2@myCompany.com"
        ]
      }
    }
  ]
}
```
Update an [Enterprise ID](glossary.html#enterpriseId) using the update command:
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
Update a user using the [createEnterpriseID](#createEnterpriseID) command and the option flag:
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
Removing a user from all their product entitlements and user-group memberships:
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
Add the Product Owner Admin role for a user:
```json
[
  {
    "user" : "jdoe@myCompany.com",
    "do" : [{
        "addRoles" : {
            "productAdmin" : ["Product1_Name"]
        }
      }]
  }
]
```
Remove the admin role for the user for a given product profile:
```json
[
  {
    "user": "jdoe@myCompany.com",
    "do": [{
        "removeRoles": {
          "admin": [ "Product1_Name"]
        }
    }]
  }
]
```

### <a name="actionRequestBodySchema" class="api-ref-subtitle">Request Body Schema</a>

#### User Command
```json
[
  {
    "do": [
      {
        "add": {
          "productConfiguration": [
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
    "user": "string"
  }
]

```
#### Usergroup Command
```json
[
  {
    "do": [
      {
        "add": {
          "productConfiguration": [
            "string"
          ],
          "user": [
            "string"
          ]
        },
        "remove": {}
      }
    ],
    "requestID": "string",
    "usergroup": "string"
  }
]

```

## Throttling

{% include apiRef/throttling.md client=10 global=100 %}