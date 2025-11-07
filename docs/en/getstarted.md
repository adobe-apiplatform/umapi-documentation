---
layout: page
title: Getting Started with User Management
nav_link: Getting Started
nav_level: 1
nav_order: 100
lang: en
---

{% include_relative partials/umIntro.md %}

The User Management API (UMAPI) allows you to manage a large number of identities programmatically, rather than individually through a user interface. You can create programs that obtain account management data stored in another identity tool that you might already be using, such as Microsoft Active Directory, and can use that data in calls to the API. You can call the API directly to perform creation, management, and removal of user accounts. You can also generate reports, or drive other processes that track which users have access to which Adobe products.

You can use the API directly to create applications and scripts to manage your organization's Adobe user accounts and product entitlements. In addition to direct programmatic access through the API, Adobe offers system administrators a ready-made user-management automation tool, [User Sync](#usersync), which is built on top of UMAPI.

Note, however, that you cannot use UMAPI to add or remove users if you are using the [Azure/Entra](https://helpx.adobe.com/enterprise/using/add-azure-sync.html) or [Google](https://helpx.adobe.com/enterprise/using/setup-sso-google.html) automated sync processes in Admin Console.

## User Management Tasks

The User Management API gives you direct access to the functionality you need to manage your Adobe user accounts and control user access to Adobe products.


### Create and Manage User Accounts

{% include_relative partials/manageUsers.md %}

### Manage Product Entitlements

{% include_relative partials/manageProductAccess.md %}

## Reporting and Analysis

You can use the UM API to collect data from your organization, and break it down by product to generate usage reports. You can get counts of the number of users in product profiles and user groups, and monitor changes over time by storing the information locally.

## <a name="usersync" class="api-ref-subtitle">Automating User Management with User Sync</a>

The [User Sync tool](https://adobe-apiplatform.github.io/user-sync.py/) can automate many of your user management tasks. User Sync is an open-source Python application provided and supported by Adobe. The tool can be invoked by your existing user-management scripts, without the need for extensive programming.

Consider this route if your enterprise uses Microsoft Active Directory or another LDAP directory service to manage and provision Adobe products, and has a large user base or high churn of users. 

User Sync is a client of the User Management API; it uses the API to automatically synchronize user data that you keep in your enterprise LDAP directory with your user data stored with Adobe. You run User Sync on the command line or from a script. Each time you run the tool it looks for differences between the user information in the two systems, and updates the Adobe side to match the enterprise directory.

## <a name="prereq" class="api-ref-subtitle">Prerequisites</a>

Before you can use the User Management API (directly or indirectly through User Sync), you must use the [Adobe Developer Console](https://developer.adobe.com/) to create a **Project**. The integration registers your application as a client of User Management API, and gives you the credentials you need to authorize calls to the API. If you plan to use the User Sync automation tool, you must create an integration to give the tool access to the API.
* For information on how to authorize calls to the User Management API, see [Authentication for API Access](UM_Authentication).  
* For complete information on the OAuth Server-to-Server implementation see [OAuth Server-to-Server credential API Reference](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/IMS/)
* For complete information on the deprecated JWT implementation, see [Service Account (JWT) Authentication](https://developer.adobe.com/developer-console/docs/guides/authentication/JWT/)

## What's Next?

* If you think your enterprise can use the ready-made API client, User Sync, read more about the tool: [Synchronize User Data with UserSync](https://adobe-apiplatform.github.io/user-sync.py/).

* If you plan to build your own API client, learn about the user-management operations that are available through the [API Overview](API_introduction.md)
* Get complete reference details for all API calls: [User Management API Reference](RefOverview.md)
* See a sample Python script and examples of representative requests: [Examples and Samples](samples/index.md)

## Need Help?

If you require further assistance for using the User Management API then please follow the instructions for Creative Cloud for Enterprise support outlined [here](https://helpx.adobe.com/uk/contact/enterprise-support.html). This will result in a support ticket being opened and assigned to our Developer Support Team.

