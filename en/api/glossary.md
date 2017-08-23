---
layout: page
nav_link: Glossary
nav_order: 601
nav_level: 2
lang: en
---

# Glossary

The following table includes common terms used throughout the User Management API documentation:

| Term | Meaning |
| :---- | :--------------- |
| Access Token | {% include apiRef/authorizationDescription.md %} |
| <a name="adminconsole" class="api-ref-subtitle">Admin Console</a> | |
| API Key | {% include apiRef/apiKeyDescription.md %} |
| Group type | The group type is returned in user-group API responses. User-groups will always be of type `USER_GROUP` |
| <a name="identity" class="api-ref-subtitle">Identity Types</a> | The [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html) resource explains the different account types available including Adobe, Enterprise and Federated IDs. |
| <a name="usergroup" class="api-ref-subtitle">User-group</a> | A group of loosely associated users. Typically used to organize a set of related users together by an organization. Examples: `U.S.FinanceOperations`, `EU Human Resources` |
| User group administrator | The user-group administrator has the ability to manage the user membership of the user groups to which they have been assigned as admin. |
| User-group ID | A unique Adobe assigned number used to identify the user-group. `46842488`|
| Organization ID | {% include apiRef/orgIdDescription.md %} |
| <a name="orgAdmin" class="api-ref-subtitle">System Administrator</a> | A "super user" for the organization who is capable of full administration capabilities including the capabilities granted to User Group, Product, Product Configuration Admin, Support and Deployment Administrators. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html) for further information. |
| <a name="usergroupAdmin" class="api-ref-subtitle">User Group Administrator</a> | Administers the user group descriptions assigned to that admin as well as all associated administrative functions including adding and removing users from groups. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
| <a name="productAdmin" class="api-ref-subtitle">Product Administrator</a> | Administers the products assigned to that admin as well as all associated administrative functions including creating product profiles and adding users and user-groups to the organization. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
| <a name="productConfigAdmin" class="api-ref-subtitle">Product Configuration Administrator</a> | Administers the Product Configuration descriptions assigned to that admin as well as all associated administrative functions including adding and removing users from Product Configurations. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
| <a name="deployment" class="api-ref-subtitle">Deployment Administrator</a> | Creates, manages, and deploys software packages and updates to end users. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
| <a name="supportAdmin" class="api-ref-subtitle">Support Administrator</a> | Non-administrative role that has access to support-related information, such as customer-reported issue reports. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information. |
{:.bordertablestyle}
