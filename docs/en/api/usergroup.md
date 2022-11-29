---
title: User Group APIs
layout: default
nav_link: User Group APIs
nav_order: 460
nav_level: 3
lang: en
---
# <a name="userGroups" class="api-ref-title">User Group APIs</a>


You cannot create either user groups or product profiles through the API. You must create them in the [Admin Console](https://adminconsole.adobe.com/enterprise/). You can then use the User Management API to manage product access for users by adding and removing users to and from your existing user groups and product profiles.

You can use a POST request to the [`action` resource](ActionsRef.md) for your organization to manage user group memberships, and to manage administrative rights in user groups. The _commands_ in the body of your POST request specify _action steps_ to take for a given _user_.

* [add](usergroupActionCommands.md#addRemove) Add a user to a specified _usergroup_
* [remove](usergroupActionCommands.md#addRemove) Remove a user from a specified _usergroup_