---
nav_link: Authentication
nav_level: 1
nav_order: 50
lang: en
---

# Authentication for API Access

To maintain the security of your applications and users, all requests to Adobe I/O APIs must be authenticated and authorized using standards such as OAuth and JSON Web Tokens (JWT). Before you can access the User Management API, you will need to obtain access credentials by creating a new Integration in the Adobe I/O Console or Admin Console.

The workflow for obtaining credentials depends on whether your app is part of a service-to-service exchange, or is meant for an end user. Apps that use the User Management API are typically service-to-service, and use the JWT workflow.

* For a service-to-service app, use the [Admin Console](https://www.adobe.io/adminconsole) to create an Integration with a JWT App Key. A member of the organization with admin rights can create the Integration. You can use the Admin Console to grant administrative privilege to users.
You will need to create or purchase a digital signing certification, and use it to sign a JSON Web Token (JWT), which you will use to authenticate your requests.
* For an end-user service that uses an Adobe API, you use the [Adobe I/O Console](https://console.adobe.io) to integrate with Adobe I/O APIs and services (such as Event notifications) with an OAuth App Key.In this case, requests must be authenticated with the app's client credentials, and the end user must also authenticate with their own Adobe ID.

For complete information about both types of integration, see [API Authentication Guide](https://www.adobe.io/content/udp/en/apis/cloudplatform/console/authentication)
