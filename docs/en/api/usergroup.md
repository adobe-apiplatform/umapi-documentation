---
title: User Group APIs
layout: default
nav_link: User Group APIs
nav_order: 440
nav_level: 2
lang: en
---

Use the following set of APIs to manage your organization's [user-groups](glossary.md#usergroup). You cannot currently create user groups programmatically. You can use the APIs to list user groups that have been created using the Admin Console, and to examine, and delete those groups.

* [Get User Groups](getUserGroups.md)
* [Get User Group](getUserGroup.md)
* [Create a new User Group](createUserGroup.md)
* [Get a list of users in a user-group](getUsersByGroup.md)
* [Update an existing User Group](updateUserGroup.md)
* [Delete a User Group](deleteUserGroup.md)

You can use the a POST request to the [`action` resource](ActionsRef.md) for your organization to manage user group memberships, and to manage administrative rights in user groups. The _commands_ in the body of your POST request specify _action steps_ to take for a given _user_.

* [add](ActionsCmds.md#add) Add a user to a specified _usergroup_
* [remove](ActionsCmds.md#remove) Remove a user from a specified _usergroup_
* [addRoles](ActionsRef.md#addRoles) Add the _admin_ role for a specified _usergroup_
* [removeRoles](ActionsRef.md#removeRoles) Remove the _admin_ role for a specified _usergroup_ 


<hr class="api-ref-rule">

