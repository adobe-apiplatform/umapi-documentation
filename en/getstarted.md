---
layout: page
title: Getting Started with User Management
nav_link: Getting Started
nav_level: 1
nav_order: 100
lang: en
---

# Getting Started with User Management

{% include umIntro.md %}

The User Management API allows you to manage a large number of identities programmatically, rather than individually through a user interface. You can create programs that obtain account management data stored in another identity tool that you might already be using, such as Microsoft Active Directory, and use that data in calls to the Adobe User Management API to perform the creation, management, and removal of user accounts, and to generate reports or drive other processes that track which users have access to which Adobe products.

You can use the API directly to create applications and scripts to manage your organization's Adobe user accounts and product entitlements. In addition to direct programmatic access through the API, Adobe offers System Administrators a ready-made user-management automation tool, [User Sync](#usersync).

## User Management Tasks

The User Management API gives you direct access to the functionality you need to manage your Adobe user accounts and control user access to Adobe products.

* **Create and Manage User Accounts**

{% include manageUsers.md %}

* **Manage Product Entitlements for your Users**

{% include manageProductAccess.md %}

## <a name="usersync" class="api-ref-subtitle">Automating User Management with User Sync</a>

If your enterprise uses Microsoft Active Directory or another LDAP directory service to manage and provision Adobe products, and has a large user base or high churn of users, the [User Sync tool](https://adobe-apiplatform.github.io/user-sync.py/) can automate many of your user management tasks. User Sync is an open-source Python application provided and supported by Adobe. The tool can be built into your existing user-management scripts, without the need for extensive programming.

User Sync is a client of the User Management API; it uses the API to automatically synchronize user data that you keep in your enterprise LDAP directory with your user data in the Adobe User Management system. You run User Sync on the command line or from a script. Each time you run the tool it looks for differences between the user information in the two systems, and updates the Adobe system to match the enterprise directory.

## <a name="prereq" class="api-ref-subtitle">Prerequisites</a>

Before you can use the User Management service, you must use the [Adobe I/O Console](https://console.adobe.io/) to create a **Service Account integration**. The integration registers your application as a client of User Management service, and gives you the credentials you need to authorize calls to the API. If you plan to use the User Sync automation tool, you must create an integration to give the tool access to the API.

To create an integration of this type, sign in to the <a href=" https://console.adobe.io">Adobe I/O Console</a> with your Enterprise ID. Your Enterprise ID must have  administrative privileges for your organization to be able to create a new Service Account integration. If you do not have the required permissions, contact an IT Administrator at your company for help. This is typically the person who distributes Creative Cloud, Acrobat or Marketing Cloud licenses within your company.  When you have completed the one-time set-up process, you can use your credentials to obtain the access token you need to begin a user-management session.

* For complete details of how to integrate your application with the User Management service, see [Service Account Authentication](https://www.adobe.io/apis/cloudplatform/console/authentication/jwt_workflow.html).

## What's Next?

* If you think your enterprise can use the ready-made API client, User Sync, read more about the tool: [Synchronize User Data with UserSync](https://adobe-apiplatform.github.io/user-sync.py/).
* If you plan to build your own API client, learn about the specific operations that are available through the User Management Web API: [Integrate User Management into an Admin Application](createapps.md)
* Get complete reference details for all API calls: [User Management API Reference](api/Overview.md)
* See a sample Python script and examples of representative requests: [Examples and Samples](samples/index.md)
