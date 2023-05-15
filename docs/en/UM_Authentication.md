---
title: Authentication for API Access
nav_link: Authentication
nav_level: 1
nav_order: 120
lang: en
layout: page
---

To maintain the security of your applications and users, all requests to Adobe I/O APIs must be authenticated and authorized using standards such as OAuth and JSON Web Tokens (JWT). Before you can access the User Management API, you will need to obtain access credentials by creating a new Integration in the Adobe I/O Console or Admin Console.


## One-time Setup

To obtain the credentials you need to access the User Management service, create a **Project** using the [Adobe Developer Console](https://developer.adobe.com/).

* Only members of the organization with SYSTEM ADMIN role can create the Integration for UMAPI. You can use the Admin Console to grant administrative privilege to users.
* For JWT workflows, you will need a keypair (public certificate and private key). One can be generated from developer portal, during the Project creation phase
* Your integration provides an API key that uniquely identifies your client, and other credentials that you need to access the UM API.


## Authorizing API calls

**Using OAuth Server-to-Server credentials**  
Obtain an access token by calling the Adobe's IMS endpoint using your Client ID and Client Secret (from the OAuth S2S enabled project on developer portal), along with with the client credentials and scope parameters.

Sample curl command:
```
curl -L -X POST 'https://ims-na1.adobelogin.com/ims/token/v2?grant_type=client_credentials&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&scope=openid,AdobeID,user_management_sdk'
```
Use the obtained access token in the Authorization header of all your other UMAPI calls along with the x-api-key header:
* **Authorization** : Bearer [access token]
* **x-api-key** : your Client ID

The access token has 24 hours validity.

**Using JWT credentials**  ----- *DEPRECATED* -----
To establish a secure service-to-service API session, you will create a JSON Web Token (JWT) that encapsulates your client credentials, and sign the JWT with the private key for a public-key certificate associated with the integration. For complete details, see [Creating a JSON Web Token](https://developer.adobe.com/developer-console/docs/guides/authentication/JWT/).

You will exchange the JWT for an access token from the Adobe Identity Management Service (IMS). Every request to an Adobe service must include the access token in the **Authorization** HTTP header, along with the API Key (client  ID) that was generated when you created the integration. Include these headers in all requests:

* **Authorization** : Bearer [access token]
* **x-api-key** : your Client ID

We recommend that you store your API client credentials and private key with strong protection, but that you do NOT store a JWT or access token. You should create a new JWT for each user-management session, and use it to obtain an access token for that session.  

To initiate each user-management session, create and send a JSON Web Token to Adobe in an access request. Include your JWT in a POST request to the Adobe Identity Management Service (IMS):
```
https://ims-na1.adobelogin.com/ims/exchange/jwt/
```
Pass the signed, base-64 encoded JWT as the value of the URL-encoded **jwt_token** parameter in the body of the POST request.

The response contains an access token that is valid for 24 hours after it is issued. Pass this token in the **Authorization** header in all subsequent requests to the User Management API.

You can request multiple access tokens. Previous tokens are not invalidated when a new one is issued. You can authorize requests with any valid access token. This allows you to overlap access tokens to ensure your integration is always able to connect to Adobe. The access token has 24 hours validity.

* For details of the log-in call, see [JWT Authentication Reference](https://developer.adobe.com/developer-console/docs/guides/authentication/JWT/#exchanging-jwt-to-retrieve-an-access-token).
* For an example of a script that creates a JWT and makes a log-in call, see [User Management Walkthrough.](samples/index.md)
