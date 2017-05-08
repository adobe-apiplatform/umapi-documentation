# Access API Reference

To establish a secure user-management session, you create a JWT that encapsulates your identity information and exchange it for an access token.
Every call to the User Management API endpoints must be authorized with this access token in the **Authorization** header, along with the API key you created when you set up your API client in the Developer Portal.

* The access token is valid for 24 hours after it is created in response to the exchange request.
* You can request multiple access tokens. Previous tokens are not invalidated when a new one is issued. You can authorize requests with any valid  access token.

## Access request syntax

Exchange your JWT for a User Management API access token by making a POST request to the Adobe identity service.

**Endpoint**: https://ims-na1.adobelogin.com/ims/exchange/jwt

## Request parameters

Pass URL-encoded parameters in the body of your POST request:

|  |  |
| --- | --- |
| **client_id** | The API key assigned to your API client account. |
| **client_secret** | The client secret assigned to your API client account. |
| **jwt_token** | The base-64 encoded JSON token that encapsulates your identity information, signed with the private key for any certificate that you have associated with your API key. |

## Responses

When a request has been understood and at least partially completed, it returns with HTTP status 200:

* **200 OK** 
	* On success, the response contains a valid access token. Pass this token in the **Authorization** header in all subsequent requests to the User Managment API. |

A failed request can result in a response with an HTTP status of 400 or 401 and one of the following error messages in the response body:

* **400** `invalid_client` 
    *  Client ID does not exist. This applies both to the `client_id`parameter and the `aud`in the JWT.
    * The `aud`field in the JWT points to a different IMS environment.
    * The `client_id`parameter and the `aud`field in the JWT do not match.
* **401**  `invalid_client` 
    * Client ID does not have the `exchange_jwt`scope. This indicates an improper client configuration. Contact support to resolve it.
    * The client ID and client secret combination is invalid.
* **400**  `invalid_token`
    * JWT is missing or cannot be decoded.
    * JWT has expired.  In this case, the `error_description`contains more details.
    * The `exp`or `jti`field of the JWT is not an integer.
* **400** `invalid_signature` 
    * The JWT signature does not match any certificate on record for given `iss`/`sub`combination
    * The signature does not match the algorithm specified in the JWT header.
* **400**  `invalid_jti`
    * The binding requires a JTI, but the `jti`field is missing or was previously used. |
* **400**  `invalid_scope` Indicates a problem with the requested scope for the token. The JWT must include `"https://ims-na1.adobelogin.com/s/ent_user_sdk": true`. Specific scope problems can be:
    * Metascopes in the JWT do not match metascopes in the binding.
    * Metascopes in the JWT do not match target client scopes.
    * Metascopes in the JWT contain a scope or scopes that do not exist.
    * The JWT has no metascopes.
* **400** `bad_request`
    * JWT payload can be decoded and decrypted but contents are incorrect. Can occur when values for fields such as `sub`, `iss`, `exp`, or `jti`are not in the proper format.

## Example

```
========================= REQUEST ==========================
POST https://ims-na1.adobelogin.com/ims/exchange/jwt
-------------------------- body ----------------------------
client_id=myClientId&client_secret=myClientSecret&jwt_token=myJSONWebToken
------------------------- headers --------------------------
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache
```

For an example of a Python script that creates and sends this type of request, see the [User Management Walkthrough](../samples/index.md).
