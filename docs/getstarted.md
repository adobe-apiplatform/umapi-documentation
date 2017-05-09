# Getting Started with User Management

The User Management API provides programmatic access to the Adobe user accounts that are associated with your organization. You can integrate this API into your organization's administrative applications and processes. You can use the API in scripts or programs to allow authorized administrators to create, update, and delete user accounts for your enterprise, and retrieve information about your Adobe users and their access to Adobe products.

The User Management API allows you to manage a large number of identities programmatically, rather than individually through a user interface. You can create programs that obtain account management data stored in another identity tool that you might already be using, such as Microsoft Active Directory, and use that data in calls to the Adobe User Management API to perform the creation, management, and removal of user accounts, and to generate reports or drive other processes that track which users have access to which Adobe products.

You can use the API directly to create applications and scripts to manage your organization's Adobe user accounts and product entitlements. In addition to direct programmatic access through the API, Adobe offers System Administrators a ready-made user-management automation tool, User Sync.

## User Management Tasks

The User Management API gives you direct access to the functionality you need to manage your Adobe user accounts and control user access to Adobe products.

* **Create and Manage User Accounts**

Creative Cloud, Marketing Cloud, and Document Cloud apps and services use an identity management system to determine an end user's entitlements. A user is recognized based on their ID. You can use the User Management API to create and manage Adobe user identities of all types. User types include the independent Adobe ID, the Enterprise ID that is managed by your enterprise but hosted by Adobe, and the Federated ID that is both managed and hosted by your enterprise. 

For details of supported types, see [Manage Identity Types](https://helpx.adobe.com/enterprise/help/identity.html) in the Enterprise help hub.

* **Manage Product Entitlements for your Users**

Users are granted access to Adobe products by adding them as members of a _product configuration_ that has been created in the [Admin Console](https://adminconsole.adobe.com/enterprise/). A product configuration identifies an Adobe product or set of products, and is associated with a list of users who are entitled to access. You can use the API to add individual users to and remove individual users from specific product configurations.

You can also create User Groups in the Admin Console. You can use the API to add and remove users to and from the user group, and to add and remove user groups to and from product configurations. This allows you to group users according to your own criteria, and then grant or deny product access to an entire group.

_Note: You cannot create or manage product configurations themselves through the User Management API. For more information about creating and managing product configurations, see [Manage Product Configurations](https://helpx.adobe.com/enterprise/help/admin-roles.html#Create_product_configurations) in the Enterprise help hub._

## Automating User Management with User Sync

If your enterprise uses Microsoft Active Directory or another LDAP directory service to manage and provision Adobe products, and has a large user base or high churn of users, the [User Sync tool](https://adobe-apiplatform.github.io/user-sync.py/) can automate many of your user management tasks. User Sync is an open-source Python application provided and supported by Adobe. The tool can be built into your existing user-management scripts, without the need for extensive programming.

User Sync is a client of the User Management API; it uses the API to automatically synchronize user data that you keep in your enterprise LDAP directory with your user data in the Adobe User Management system. You run User Sync on the command line or from a script. Each time you run the tool it looks for differences between the user information in the two systems, and updates the Adobe system to match the enterprise directory.

## Prerequisites

Before you can use the User Management service, you must use the [Adobe I/O Console](https://console.adobe.io/) to create a **Service Account integration**. The integration registers your application as a client of User Management service, and gives you the credentials you need to authorize calls to the API. If you plan to use the User Sync automation tool, you must create an integration to give the tool access to the API.

To create an integration of this type, sign in to the <a href=" https://console.adobe.io">Adobe I/O Console</a> with your Enterprise ID. Your Enterprise ID must have  administrative privileges for your organization to be able to create a new Service Account integration. If you do not have the required permissions, contact an IT Administrator at your company for help. This is typically the person who distributes Creative Cloud, Acrobat or Marketing Cloud licenses within your company.  When you have completed the one-time set-up process, you can use your credentials to obtain the access token you need to begin a user-management session.

* For complete details of how to integrate your application with the User Management service, see [Service Account Authentication](https://www.adobe.io/apis/cloudplatform/console/authentication/jwt_workflow.html).

## What's Next?

* If you think your enterprise can use the ready-made API client, User Sync, read more about the tool: [Synchronize User Data with UserSync](https://adobe-apiplatform.github.io/user-sync.py/).
* If you plan to build your own API client, learn about the specific operations that are available through the User Management Web API: [Integrate User Management into an Admin Application](createapps.md)
* Get complete reference details for all API calls: [User Management API Reference](api/Overview.md)
* See a sample Python script and examples of representative requests: [Examples and Samples](samples/index.md)
