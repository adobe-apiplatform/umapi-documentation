---
title: User Group Management Action Commands
layout: default
nav_link: User Group Action Commands
nav_order: 402
nav_level: 3
lang: en
---

# User Group Management Action Commands

Each _command_ entry begins with a _root command_ that specifies whether a set of actions applies to an individual user, 
or to a [user group](glossary.md#usergroup). Use the __usergroup__ root command to manage user groups. You can operate on a maximum of 10 user-groups per request.

The `do` list for a `usergroup` entry specifies the series of _steps_ to complete for the group. The steps can perform group-management operations (create, delete, update) or membership operations (add and remove members and entitlements). You can add product profiles to a user group, giving all user group members the related entitlements. 

## <a name="user-group-information" class="api-ref-subtitle">Management Step Actions for User Groups</a>

* To create, update or delete a group, specify `createUserGroup`, `updateUserGroup`, or `deleteUserGroup` steps in the `do` list for a `usergroup` entry. 

* To change provisioning through group membership, specify the `add` and `remove` steps in the `do` list for a `usergroup` entry to update the membership lists for the user group.

### <a name="createUserGroup" class="api-ref-subtitle">__createUserGroup:__</a>

Creates a user group, or updates the description if the named group already exists group. There can be only one create operation for a given `usergroup` command entry, and it must be the first step.
 
```json
{
  "createUserGroup": {
    "name": "string",
    "description": "string",
    "option": "string"
  }
}
```

* __name:__ _string_; Required. The name of the user group.
* __description:__ _string_; Optinal. The description of the usergroup.
* __option:__ _string_, possible values: `{ignoreIfAlreadyExists, updateIfAlreadyExists}`; Optional for `createUserGroup` action. Specifies how to perform the create operation when a user group with the given name already exists in the user database.  
  - `ignoreIfAlreadyExists`: If the user group already exists, ignore the _create_ step but process any other steps in the command entry for this user.
  - `updateIfAlreadyExists`: If the user group already exists, update the `description` of the existing group with the provided value (if any), but ignore the `name`  value. After the update, process any other steps in the command entry for this group.

### <a name="updateUserGroup" class="api-ref-subtitle">__updateUserGroup:__</a>

Updates the name or description user group. Both fields are optional.

See [user-group-information](#user-group-information) for individual field descriptions.
```json
{
  "updateUserGroup": {
    "name": "string",
    "description": "string"
  }
}
```

### <a name="deleteUserGroup" class="api-ref-subtitle">__deleteUserGroup:__</a>

Deletes an existing user group. No further steps are performed after deletion.

```json
{
  "deleteUserGroup": {
  }
}
```

### <a name="addRemove" class="api-ref-subtitle">Adding and removing memberships for a user group</a>

A group has two membership lists: users who are members of the group, and product profiles for which the group has access. In the `add` and `remove` actions, supply the `user` option with a list of users to update the group membership, and the `productConfiguration` option with a list of product profile names.

* When you add a user to the group, that user gains entitlement for all member product profiles. 
When you remove a user from the group, that user loses the associated entitlements (unless they have individual access).

* When you add a product profile, all of the member users gain the associated entitlements.
When you remove a product profile, all of the users in the user group lose the associated entitlements (unless they have individual access). Please note that you cannot use the add command if the user-group has more than 200,000 users.

* When a group has `isReadOnly` set to true, you cannot add or remove users from the group however you can add or remove product profiles.

>NOTE: Use the [`group`](group.md) resource to retrieve information about defined groups.

Each step can add or remove up to 10 memberships in one command entry using the `user` and `productConfiguration` options. Specify users by email, and product profiles by name. 

```json
{
  "usergroup": "DevOps",
  "do": [
     {
      "add": {
        "user": [
          "user1@myCompany.com"
        ],
        "productConfiguration": [
          "Profile1_Name"
        ],
      }
     },
     {
      "remove": {
        "user": [
          "user2@myCompany.com"
        ],
        "productConfiguration": [
          "Profile2_Name"
        ],        
       }
     }
  ]
}
```

<hr class="api-ref-rule">

## <a name="groupExamples" class="api-ref-subtitle">Usergroup command request body schema</a>

```json
[
  {
    "do": [
      {
         "createUserGroup": {
           "option": "string",
           "description": "string"
         }
      },
      {
        "updateUserGroup": {
          "name": "string",
          "description": "string"
        }
      },
      {
        "deleteUserGroup" : {}
      },
      {
        "add": {
          "user": [
            "string"
          ],
          "productConfiguration": [
            "string"
           ]
       },
      }
      {
        "remove": {}
      }
   ],
    "requestID": "string",
    "usergroup": "string"
  }
]
```
<hr class="api-ref-rule">

## User-group action examples

Add a product profile and a user to a user group, and remove another product profile and user.

```json
{
  "usergroup": "DevOps",
  "do": [
      {
        "add": {
         "user": [
           "user1@myCompany.com"
         ],
          "productConfiguration": [
            "Profile1_Name"
         ] 
        } 
      },
      {
        "remove": {
          "user": [
            "user2@myCompany.com"
           ],
          "productConfiguration": [
            "Profile2_Name"
         ]
         }
       }
  ]
}
```

Update a usergroup's name and description.

```json
{
  "usergroup": "DevOps",
  "do": [
    {
      "updateUserGroup" : {
        "description": "Devops group description",
        "name": "DevOps Team"
      }
    }
  ]
}
```

Update a usergroup and add production profile.

```json
{
  "usergroup": "DevOps",
  "do": [
    {
      "updateUserGroup" : {
         "description": "Devops group description",
         "name": "DevOps Team"
       }
      },
    {
      "add": {
        "user": [
          "user1@myCompany.com"
        ]
       }
     }
  ]
}
```

Delete a usergroup.

```json
[
  {
    "requestID": "dsctesting",
    "usergroup": "DevOps Team",
    "do": [
      {
        "deleteUserGroup": {
        }
      }
    ]
  }
]
```

