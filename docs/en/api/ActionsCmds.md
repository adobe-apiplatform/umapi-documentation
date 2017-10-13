---
title: User Management Action Commands
layout: default
nav_link: User Action Commands
nav_order: 401
nav_level: 3
lang: en
---

# User Management Action Commands

The JSON _commands_ structure contained in your POST request to the `action` endpoint specifies a sequence of commands. Each command entry specifies a user or a [user group](glossary.md#usergroup) and a sequence of _steps_ to be performed for that user or user group.

For a given command entry, the API attempts to perform the steps in the order that they appear. However, the order of execution of commands is not always guaranteed. If the same user or user group is listed in more than one command, results could differ depending on the order of command execution. Use the following order as guidance:

* Creates ([addAdobeId](ActionsCmds.md#addAdobeID), [createEnterpriseID](ActionsCmds.md#createEnterpriseID), [createFederatedID](ActionsCmds.md#createFederatedID)).
* [Updates](ActionsCmds.md#update) of users' information.
* [Removal](ActionsCmds.md#remove) of entitlements and memberships.
* [Removal](ActionsCmds.md#removeRoles) of administrative roles
* [Adding](ActionsCmds.md#add) of entitlements and memberships
* [Adding](ActionsCmds.md#addRoles) of administrative roles
* [Removal](ActionsCmds.md#removeFromOrg) of users from an organization

******

# <a name="actionRequestBodyProperties" class="api-ref-subtitle">Command entries</a>

Each _command_ entry begins with a _root command_ that specifies whether a set of actions applies to an individual user, or to a user group. The JSON commands structure allows a maximum of 10 users or user-groups to be operated on per request.

## Root commands

<a name="userRootCommand" class="api-ref-subtitle">__user:__</a> _string_
The user field is usually an email address with a UID and domain component `jdoe@example.com`. Organizations can be configured to accept usernames that are not email addresses. In these cases, the `domain` property must be provided in order to identify the user. [Identity Types](glossary.md#identity) explains the different account types available. 

<a name="usergroupRootCommand" class="api-ref-subtitle">__usergroup:__</a> _string_
To update the membership list for a given [user group](glossary.md#usergroup), specify `add` and `remove` actions in the `do` list for the `usergroup`. See [Step Actions for User Groups](#groupStepActions).

__do:__
Within a command's `do` entry, a set of _step actions_ specify what management operations to perform for the root user or user group.

<hr class="api-ref-rule">

## Step actions for users

This section describes step actions that can be performed for a [user](#userRootCommand). For steps that can be performed for a [user group](#usergroupRootCommand), see [User Group Step Actions](#groupStepActions).

The following properties apply to a [user](#userRootCommand):

__requestID:__ _string_
Arbitrary string to be returned in the response payload. This is to help identify the response that corresponds to a particular command entry.

__domain:__ _string_ 
[Federated IDs](glossary.md#federatedId) that are not email addresses, must supply the domain the user belongs to in order to identify the user. This is required for all operations; create, update, add, remove, and removeFromOrg.
The domain field must be at the same level as the user field. The domain field is ignored if the user has an [Adobe](glossary.md#adobeId) or [Enterprise](glossary.md#enterpriseId) ID. [Identity Types](glossary.md#identity) explains the different account types available.

__useAdobeID:__ _boolean_ 
When true, the user ID is interpreted to refer to an existing [Adobe ID](glossary.md#adobeId) even if a [Enterprise](glossary.md#enterpriseId) or [Federated ID](glossary.md#federatedId) exists with the same name.

__do:__
Lists the series of _steps_ to complete for this command entry. For a single user command entry, there can be only __one__ create user operation ([createEnterpriseID](#createEnterpriseID), [createFederatedID](#createFederatedID) or [addAdobeID](#addAdobeID)) and __one__ delete user operation ([removeFromOrg](#removeFromOrg)).


### <a name="addAdobeID" class="api-ref-subtitle">__addAdobeID:__</a>
Adds a user who has an existing [Adobe ID](glossary.md#adobeId). User-information fields such as `firstname` and `lastname` can be included.   

>Previously, when an Adobe ID user was added, the user would receive an email inviting them to join the organization.

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

### <a name="createEnterpriseID" class="api-ref-subtitle">__createEnterpriseID:__</a> 
Creates an [Enterprise ID](glossary.md#enterpriseId). See [user-information](#user-information) for individual field descriptions.
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

### <a name="createFederatedID" class="api-ref-subtitle">__createFederatedID:__</a> 
Creates a [Federated ID](glossary.md#federatedId). See [user-information](#user-information) for individual field descriptions.
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
### <a name="user-information" class="api-ref-subtitle">__User Information Fields__</a>
* __firstname:__ _string_; Limited to 250 characters. Required for `createEnterpriseID` and `createFederatedID`. Optional for `addAdobeID`.
* __lastname:__ _string_; Limited to 250 characters. Required for `createEnterpriseID` and `createFederatedID`. Optional for `addAdobeID`.
* __email:__ _string_; A valid email address. Required for `createEnterpriseID`, `addAdobeID` and `createFederatedID`.
* __country:__ _string_; A valid ISO 2-character country code. Optional for `createEnterpriseID` and `addAdobeID`. Required for `createFederatedID`. The `country` value cannot be updated after it is set.
* __option:__ _string_, possible values: `{ignoreIfAlreadyExists, updateIfAlreadyExists}`; In addition to the new user's field values, the parameters can include an _option_ flag that specifies how to perform the create operation when a user with the given ID already exists in the user database. Default behaviour is `ignoreIfAlreadyExists`. Optional property for `createEnterpriseID`, `createFederatedID`, `addAdobeID`.
  - `ignoreIfAlreadyExists`: If the ID already exists, ignore the _create_ step but process any other steps in the command entry for this user.
  - `updateIfAlreadyExists`: If the ID already exists, perform an _update_ action using the parameters in the create step. After updating all fields present in the step, process any other steps in the command entry for this user.

### <a name="update" class="api-ref-subtitle">__update:__</a> 
The `update` action writes new personal information to the user's account details. You can update [Enterprise](glossary.md#enterpriseId) and [Federated IDs](glossary.md#federatedId) that are managed by your organization.
Independent [Adobe IDs](glossary.md#adobeId) are managed by the individual user and cannot be updated through the User Management API. Attempting to update information for a user who has an [Adobe ID](glossary.md#adobeId) will result in error [error.update.adobeid.no](ErrorRef.md#adobeidno).
For [Federated IDs](glossary.md#federatedId), the `update` request can only change the information that is stored by Adobe. You cannot change information your organization stores outside of Adobe through the User Management API. You can, however, include a `username` field for users whose email address is in your domain. The `username` value must not include an at-sign character (@). The parameters of an update step specify the changed fields and their new values. If you do not specify a field, its value remains unchanged.
[Identity Types](glossary.md#identity) explains the different account types available. See [user-information](#user-information) for individual field descriptions.
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

### <a name="add" class="api-ref-subtitle">__add:__</a>
Enables the entitlement or membership of users to [product profiles](glossary.md#productProfile) and [user groups](glossary.md#usergroup). Product profiles correspond to specific product access rights, so adding product access for a user is the same as adding that user to the corresponding product profile. You can add a maximum of 10 memberships in one command entry. See [Add attributes](#addRemoveAttr) section for full details of the following attributes:
```json
{
  "add": {
    "productConfiguration": [
      "product_profile_name"
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

### <a name="remove" class="api-ref-subtitle">__remove:__</a>
Removes the entitlement or membership of users from product profiles and [user-groups](glossary.md#usergroup). Product profiles correspond to specific product access rights, so removing product access for a user is the same as removing that user from the corresponding product profile. You can remove a maximum of 10 memberships in one command entry, unless you use the special  "all" parameter to remove all memberships for the user or user-group. See [Remove attributes](#addRemoveAttr) section for full details of the following attributes:
```json
{
  "remove" : {
    "productConfiguration": [
      "product_profile_name"
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
Additionally you can pass the attribute `all` to remove the user from all groups including product configs and user-groups:
```json
{
  "remove" : "all"
}
```
### <a name="addRemoveAttr" class="api-ref-subtitle">__Add/Remove Attributes__</a>
* __group:__; A list of product configs with a maximum of 10 entries. This can be used with the `user` or `usergroup` root commands and is available in the [add](#add) and [remove](#remove) operations.

* __usergroup:__; A list of user groups with a maximum of 10 entries. This can be used with the `user` root command and is available in the [add](#add) and [remove](#remove) operations.

* __user:__; A list of users with a maximum of 10 entries. This can be used with the `usergroup` root command and is applicable to the [add](#add) and [remove](#remove) operations.

### <a name="addRoles" class="api-ref-subtitle">__addRoles:__</a>

Grant administrative privileges to the product profile or user group for the specified user. See [Add Role attributes](#addRemoveRoleAttr) section for full details of the following attributes:
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

### <a name="removeRoles" class="api-ref-subtitle">__removeRoles:__</a>

When a user is a member of a product profile, this command will revoke administrative privileges for that user in that product profile or user group. See [Remove Role attributes](#addRemoveRoleAttr) section for full details of the following attributes:
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
### <a name="addRemoveRoleAttr" class="api-ref-subtitle">__Add/Remove Role Attributes__</a>
* __productAdmin:__; A list of products (with a maximum of 10 entries) to assign the user as a [Product Administrator](glossary.md#productAdmin). This can only be used with the `user` root command and is applicable to the `addRoles` and `removeRoles` operations.

* __admin:__; A list of product profiles and user groups (with a maximum of 10 entries) to assign the user as an Administrator. This can only be used with the `user` root command and is applicable to the `addRoles` and `removeRoles` operations. Possible roles include:
  * "org": Assign the user as a [System Administrator](glossary.md#orgAdmin).
  * "deployment": Assign the user as a [Deployment Administrator](glossary.md#deployment).
  * "support": Assign the user as a [Support Administator](glossary.md#supportAdmin).
  * "{product-profile-name}": Assign user as a [Product Profile Administrator](glossary.md#productProfileAdmin).
  * "{user-group-name}": Assign user as a [UserGroup Administrator](glossary.md#usergroupAdmin).
```json
  {
      "addRoles": {
        "admin": [
          "org"
        ]
      }
  }
```

### <a name="removeFromOrg" class="api-ref-subtitle">__removeFromOrg:__</a>

Removes the user's membership in the organization, and optionally from membership in a domain that is linked to the given organization through the trusted-domain relationship. This includes any product configs and user-groups in the organization that they are a member of. There can only be a single `removeFromOrg` action in a command entry. If present, the removal action will be the last step invoked. If the user is specified by email address, then the domain of the email address specifies the domain of the account. If the user is specified by Username, the domain must be provided.
```json
{
  "removeFromOrg": {
    "deleteAccount": boolean
  }
}
```

* __deleteAccount:__ _boolean_; If true then if the account is owned by the organization, the account is also deleted. Note that [Adobe IDs](glossary.md#adobeId) are never deleted because they are owned by the user, not the organization. The default value is false.

<hr class="api-ref-rule">

## <a name="groupStepActions" class="api-ref-subtitle">Step Actions for User Groups</a>

To change provisioning through user-group and profile membership, use the root command  __usergroup:__ in an action request.  In the `do` list for the group, use the `add` and `remove` actions to update the membership lists for the group. 

A group has two membership lists: users who are members of the group, and product profiles for which the group has access. In the `add` and `remove` actions, supply the `user` option with a list of users to update the group membership, and the `productConfiguration` option with a list of product profiles to update the group's entitlements. 

* When you add a user to the group, that user gains access to that group's product profiles.   
When you add a profile to the group, all of the group members gain access to that profile.

* When you remove a member from the group, that member loses access to the group's profiles.  
When you remove a profile from the group, all of the group's members lose access to the profile (unless they have individual access).

### Adding and removing memberships for a user group

When the root command is "usergroup", the "do" list can contain "add" and "remove" steps. Each step can add or remove a set of  "user" entries specified by email, and a set of "productConfiguration" (profile) entries, specified by name. 

Up to 10 memberships can be added or removed in one command entry using the `user` and `productConfiguration` options.

```json
{
  "usergroup": "DevOps",
  "do": [
    {
      "add": {
        "productConfiguration": [
          "Profile1_Name"
        ],
        "user": [
          "user1@myCompany.com"
        ]
      },
      "remove": {
        "productConfiguration": [
          "Profile2_Name"
        ],
        "user": [
          "user2@myCompany.com"
        ]
      }
    }
  ]
}
```

<hr class="api-ref-rule">

## <a name="actionRequestBodyExamples" class="api-ref-subtitle">Request Body Schemas and Examples</a>

The following sections provide examples of request bodies for user and user-group management actions.

* [User action schema and examples](#userExamples)
* [User-group action schema and examples](#groupExamples)

### <a name="userExamples" class="api-ref-subtitle">User command request body schema</a> 
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

### User action examples

Create a [Federated ID](glossary.md#federatedId) and add the user to the Product Profiles 'Photoshop' and 'Illustrator', then remove them from the user group 'devOps'. The user is identified by passing the username and domain.
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
Create an [Enterprise ID](glossary.md#enterpriseId):
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

Update an [Enterprise ID](glossary.md#enterpriseId) using the update command:
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
Remove a user from all their product entitlements and user-group memberships:
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
Remove the admin role for the user for a given product config:
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

## <a name="groupExamples" class="api-ref-subtitle">Usergroup command request body schema</a> 
 
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

### User-group action examples </a>

Add a product profile and a user to a user group, and remove another product profile and user.

```json
{
  "usergroup": "DevOps",
  "do": [
    {
      "add": {
        "productConfiguration": [
          "Profile1_Name"
        ],
        "user": [
          "user1@myCompany.com"
        ]
      },
      "remove": {
        "productConfiguration": [
          "Profile2_Name"
        ],
        "user": [
          "user2@myCompany.com"
        ]
      }
    }
  ]
}
```
