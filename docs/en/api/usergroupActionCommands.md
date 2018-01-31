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

The `do` list for a `usergroup` entry specifies the series of _steps_ to complete for the group. The steps can perform membership operations (add and remove member users).

## <a name="groupStepActions" class="api-ref-subtitle">Membership Step Actions for User Groups</a>

To change provisioning through user-group and profile membership, use the root command  __usergroup:__ in an action request.
In the `do` list for the group, use the `add` and `remove` actions to update the membership lists for the group.

A group has two membership lists: users who are members of the group, and product profiles for which the group has access. In the `add` and `remove` actions, supply the `user` option with a list of users to update the group membership, and the `productConfiguration` option with a list of product profiles to update the group's entitlements.

* When you add a user to the group, that user gains access to that group's product profiles.
When you add a profile to the group, all of the group members gain access to that profile.

* When you remove a member from the group, that member loses access to the group's profiles.
When you remove a profile from the group, all of the group's members lose access to the profile (unless they have individual access).

### Adding and removing memberships for a user group

When the root command is "usergroup", the "do" list can contain "createUserGroup", "add" and "remove" steps. Each step can add or remove a set of  "user" entries specified by email, and a set of "productConfiguration" (profile) entries, specified by name.

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
      }
     },
     {
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
        }
      },
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
          "productConfiguration": [
            "Profile1_Name"
         ],
         "user": [
           "user1@myCompany.com"
         ]
        } 
      },
      {
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

