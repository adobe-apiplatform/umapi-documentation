---
layout: page
title: API Overview
nav_link: API Overview
nav_level: 1
nav_order: 135
lang: en
---
# API Overview

## User Management Tasks

To manage Adobe users in your organization, your applications can use the User Management API to create, update, and delete user accounts of different _identity types_. For a complete discussion of the different account types, see [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html).

You can use the API to perform a variety of user-management tasks:

* Update user information associated with an Enterprise ID or Federated ID account that is managed by your organization. Adobe ID accounts are managed by the user and by Adobe.
* Remove accounts of any type from your organization. For Enterprise IDs, you can also delete the accounts.
* Query your Adobe users.
* Manage membership in user groups and product profiles. These memberships control user access to Adobe products.
* Manage administrative rights for users within user groups and product profiles.

This page provides an introduction to the endpoints and techniques you use to perform these tasks. For complete syntax details, see the [UM API Reference](RefOverview.md).

## Calling into the UM API

Before you can make calls into the User Management API, you must obtain proper credentials. See [Authentication for API Access](UM_Authentication.md). You use your access credentials to authorize all calls into the UM API.

Address all user-management requests to the UM API server:

```
https://usermanagement.adobe.io/v2/usermanagement/...
```

For a Python code walkthrough and samples of actual API calls that demonstrate most user management tasks, see the [User Management Walkthrough](samples/index.md).

********

# Introduction to User Management APIs

* [Manage your Adobe Users](#manage-your-adobe-users)
When you have obtained access, you can use the API to request changes to your Adobe user accounts.
   * [Query Users](#query-users)  
   You can retrieve information about users in your organization.
   * [Manage User Groups](#manage-user-groups)  
   You can now create, delete, and update user groups programmatically, as well as through the [Admin Console](https://adminconsole.adobe.com/enterprise).
   
* [Manage Products Access and Admin Rights](#manage-products)  
Product access is controlled by memberships in user groups and product profiles. You can use the API to query and update memberships, and control user roles within the groups. 

* [Throttling and Error Handling](#throttling-and-error-handling)  
Throttling enables you to handle errors that result from data-access limitations.

*****

## <a name="manage-your-adobe-users" class="api-ref-subtitle">Manage your Adobe Users</a>

The API defines a set of specific write _actions_ that you use to create, update, and delete user accounts, and manage Adobe product access for users. To make most user-management requests, send an HTTPS POST request to the user-management [Action API](api/ActionsRef.md):

```
https://usermanagement.adobe.io/v2/usermanagement/action/{orgId}
```

* Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".

You specify actions for specific users in the JSON body of a POST request to the `action` endpoint for your organization. The JSON structure specifies a set of _commands_. Each command names a user or user group, and specifies one or more _action steps_ to take for that user or group. A single request can include commands for multiple users or groups. An optional _test mode_ allows you to check a set of commands for validity without making any actual changes in your user data.

You can also use this POST request to manage administrative rights for users in user groups and product profiles.

* For detailed syntax of action requests, see [User Management Action Requests](api/ActionsRef.md).
* For detailed syntax of the JSON commands structure and a full description of user account operations, see [User Management Action Commands](api/ActionsCmds.md).
* For a full description of user group operations, see [User Group Management Action Commands](api/usergroupActionCommands.md).


### Adding Users with Adobe ID Identity Type

You can add users with any of the three identity types: Enterprise, Federated ID, or Adobe ID. See a full discussion at [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html).  

When you create a new user of the Adobe ID type, the user is identified by email address. The Adobe ID can already exist or be created. The new user is immediately added to your organization, and sent an email that gives them the option to be removed from the organization, or to update their user profile.

 > Previously, users were required to accept an email invitation before being added to your organization. A deprecated API allowed you to [manage pending new-user invites](api/ManageInvites.md). Please discontinue use of this API in your applications.
 
### <a name="query-users" class="api-ref-subtitle">Query Users</a>

You can retrieve paged lists of all users for the organization, and examine information for an individual user through the unique user ID. [See User Access APIs](api/user.md).

### <a name="manage-user-groups" class="api-ref-subtitle">Manage User Groups</a>

You can create new user groups programmatically, update the names and descriptions of existing user groups, and delete user groups, through the [Action API](api/usergroupActionCommands.md).

***
## <a name="manage-products" class="api-ref-subtitle">Manage Product Access and Admin Rights</a>

Users are provisioned for access to Adobe products through their membership in user groups and product profiles. A user group is a collection of users who share a set of permissions. Both individual users and user groups can be added to product profiles to give them access to a set of products.  

You cannot create product profiles through the API. You must create them in the [Admin Console](https://adminconsole.adobe.com/enterprise/). You can then use the User Management API to manage product access for users by adding and removing users to and from your existing user groups and product profiles.

### Manage memberships and roles

* To manage user group membership and assign administrative rights in user groups, use the `usergroup` root command in a POST request to the [Action API](api/ActionsCmds.md) for your organization. For details, see [User Group Management Actions](api/usergroupActionCommands.md).  
```
https://usermanagement.adobe.io/v2/usermanagement/action/{orgId}
```
* To manage product profile membership and administrative rights, use the `user` root command in a POST request to the [Action API](api/ActionsCmds.md) for your organization. Use the [Product Information APIs](api/product.md) to find products and profiles for your organization.  
```
https://usermanagement.adobe.io/v2/usermanagement/{orgId}/product/{productId}/configurations/{profileId}
```

***********
## <a name="throttling-and-error-handling" class="api-ref-subtitle">Throttling and Error Handling</a>

To protect the availability of the Adobe back-end user identity systems, the User Management API imposes limits on client access to the data. Limits apply to the number of calls that an individual client can make within a time interval, and global limits apply to access by all clients within the time period.

Please refer to the _Throttling_ section of each API to determine its limitations. When the access limit is reached, further calls fail with **429 Too Many Requests**.

If you are leveraging the [User Sync Tool](https://adobe-apiplatform.github.io/user-sync.py/en/user-manual/configuring_user_sync_tool.html), our recommendation is to run the tool no more than once every 2 hours. Further information on scheduling recommendations can be found in their [Deployment Best Practices](https://adobe-apiplatform.github.io/user-sync.py/en/user-manual/deployment_best_practices.html) section.
