---
layout: page
nav_link: Glossary
nav_order: 500
nav_level: 1
lang: en
---

# Glossary

The following table defines common terms used throughout the User Management API documentation:

| Term | Meaning |
| :---- | :--------------- |
| Access Token | {% include_relative partials/authorizationDescription.md %} |
| <a name="adminconsole" class="api-ref-subtitle">Admin Console</a> | A central location for managing your Adobe entitlements across your entire organization, available at https://adminconsole.adobe.com/enterprise. |
| <a name="adobeId" class="api-ref-subtitle">AdobeID</a> | An Identity Type that is created, owned, and managed by the end user. Adobe performs authentication, and the end user manages the identity. Users retain complete control over files and data associated with their ID. See full discussion at [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html). |
| API Key | {% include_relative partials/apiKeyDescription.md %} |
| <a name="deployment" class="api-ref-subtitle">Deployment Administrator</a> | Creates, manages, and deploys software packages and updates to end users. See full discussion at [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#).|
| <a name="enterpriseId" class="api-ref-subtitle">Enterprise ID</a> | An Identity Type that is created, owned, and managed by an organization. Adobe hosts the Enterprise ID and performs authentication, but the organization maintains the Enterprise ID. End-users cannot sign up and create an Enterprise ID, nor can they sign up for additional products and services from Adobe using an Enterprise ID. See full discussion at [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html). |
| <a name="federatedId" class="api-ref-subtitle">Federated ID</a> | An Identity Type that is created and owned by an organization, and linked to the enterprise directory through federation. The organization manages credentials and processes Single Sign-On through a SAML2 identity provider. See full discussion at [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html). |
| <a name="unknownUserType" class="api-ref-subtitle">usertype `unknown`</a> | In some cases a userType may contain the value `unknown`. In these cases the user may not contain the necessary values to identify the user type.|
| Group type | The group type is returned in user-group API responses. User-groups are always of type `USER_GROUP` |
| <a name="identity" class="api-ref-subtitle">Identity Types</a> | The [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html) resource explains the different account types that are available: Adobe, Enterprise, and Federated IDs. |
| Organization ID | {% include_relative partials/orgIdDescription.md %} |
| <a name="productAdmin" class="api-ref-subtitle">Product Administrator</a> | A user role in an organization. A user with this role (an admin) administers the assigned products, managing all associated administrative functions, such as creating product profiles and adding users and user-groups to the organization. See full discussion at [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#). |
| <a name="productConfigAdmin" class="api-ref-subtitle">Product Profile Administrator</a> | A user role in an organization. A user with this role administers assiged Product Profile descriptions, managing all associated administrative functions, such as adding and removing users from Product Profiles.  See full discussion at [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#). |
| <a name="orgAdmin" class="api-ref-subtitle">System Administrator</a> | A user role in an organization. A "super user" for the organization who is allowed to perform all administrative tasks, including the capabilities granted to User Group admin, Product admin, Product Profile admin, Support admin and Deployment admin. See full discussion at [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#). |
| <a name="usergroup" class="api-ref-subtitle">User-group</a> | A group of loosely associated users. Typically used to organize a set of related users by department or function. For example: `U.S.FinanceOperations`, `EU Human Resources` |
| User-group ID | A unique Adobe-assigned number used to identify a user-group. For examples, `46842488`|
| <a name="usergroupAdmin" class="api-ref-subtitle">User-group Administrator</a> | A user role in an organization. Administers assigned user-group descriptions, managing all associated administrative functions, such as adding and removing users from groups. See full discussion at [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#). |
{:.bordertablestyle}
