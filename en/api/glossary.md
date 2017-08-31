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
| <a name="adobeId" class="api-ref-subtitle">AdobeID</a> | An Adobe ID is created, owned, and managed by the end user. Adobe performs the authentication and the end user manages the identity. Users retain complete control over files and data associated with their ID. Full information available at [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html). |
| API Key | {% include apiRef/apiKeyDescription.md %} |
| <a name="deployment" class="api-ref-subtitle">Deployment Administrator</a> | Creates, manages, and deploys software packages and updates to end users. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
| <a name="enterpriseId" class="api-ref-subtitle">Enterprise ID</a> | An Enterprise ID is created, owned, and managed by an organization. Adobe hosts the Enterprise ID and performs authentication, but the organization maintains the Enterprise ID. End-users cannot sign up and create an Enterprise ID, nor can they sign up for additional products and services from Adobe using an Enterprise ID. Full information available at [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html). |
| <a name="federatedId" class="api-ref-subtitle">Federated ID</a> | Federated ID is created and owned by an organization, and linked to the enterprise directory via federation. The organization manages credentials and processes Single Sign-On via a SAML2 identity provider. Full information available at [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html). |
| Group type | The group type is returned in user-group API responses. User-groups will always be of type `USER_GROUP` |
| <a name="identity" class="api-ref-subtitle">Identity Types</a> | The [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html) resource explains the different account types available including Adobe, Enterprise and Federated IDs. |
| Organization ID | {% include apiRef/orgIdDescription.md %} |
| <a name="productAdmin" class="api-ref-subtitle">Product Administrator</a> | Administers the products assigned to that admin as well as all associated administrative functions including creating product profiles and adding users and user-groups to the organization. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
| <a name="productConfigAdmin" class="api-ref-subtitle">Product Configuration Administrator</a> | Administers the Product Configuration descriptions assigned to that admin as well as all associated administrative functions including adding and removing users from Product Configurations. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
| <a name="orgAdmin" class="api-ref-subtitle">System Administrator</a> | A "super user" for the organization who is allowed to perform all administrative tasks including the capabilities granted to User Group admin, Product admin, Product Configuration admin, Support admin and Deployment admin. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html) for further information. |
| <a name="supportAdmin" class="api-ref-subtitle">Support Administrator</a> | Non-administrative role that has access to support-related information, such as customer-reported issue reports. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information. |
| <a name="usergroup" class="api-ref-subtitle">User-group</a> | A group of loosely associated users. Typically used to organize a set of related users together by an organization. Examples: `U.S.FinanceOperations`, `EU Human Resources` |
| User-group ID | A unique Adobe assigned number used to identify the user-group. `46842488`|
| <a name="usergroupAdmin" class="api-ref-subtitle">User-group Administrator</a> | Administers the user-group descriptions assigned to that admin as well as all associated administrative functions including adding and removing users from groups. See [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html#) for further information.|
{:.bordertablestyle}
