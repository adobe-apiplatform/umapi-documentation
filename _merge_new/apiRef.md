# Adobe: User Management API
__Version:__ 2.2.23

# APIs

| Path | Operation| Overview |
| --------------------- | --- | ------------ |
| [/v2/usermanagement/organizations/{orgId}/users/{userString}](#getUserByEmailOrUsername) | GET | Gets details for a single user within an organization. |
| [/v2/usermanagement/{orgId}/user-groups](usergroup.md#getUserGroups) | GET | Gets a paginated list of user-groups. |
| [/v2/usermanagement/{orgId}/user-groups/{groupId}](usergroup.md#getUserGroup) | GET | Gets details for a single user-group within an organization. |
| [/v2/usermanagement/{orgId}/user-groups](usergroup.md#createUserGroup) | POST | Create a new user-group for the given organization with a name and description. |
| [/v2/usermanagement/{orgId}/user-groups/{groupId}](usergroup.md#updateUserGroup) | PUT | Update name and/or description for the given user-group of the given organization. |
| [/v2/usermanagement/{orgId}/user-groups/{groupId}](usergroup.md#deleteUserGroup) | DELETE | Delete the given user-group identified from the given organization. |
| [/v2/usermanagement/action/{orgId}](action.md#action) | POST | Batch create, update, entitle, and remove users operations for an organization |

# <a href="getUserByEmailOrUsername">GET /v2/usermanagement/organizations/{orgId}/users/{userString}</a>

This API retrieves the details of a single user within a specified organization by searching for them using their email address or a username and domain combo. Successful queries will return a 200 response whose body is a single JSON response representing the user information.  

### Example Requests:
Searching by email for Type 1, Type 2 or Type 3 email-federated users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching by username for Type 3 username-federated users:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe?domain=example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching for Type 1 user with domain:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=AdobeID \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching for Type 2 or Type 3 email-federated users with domain parameter included:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching for users in a multi-domain directory:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=my-domain.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
___

## Parameters

| Name | Description | Type | Data Type| Required |
| --- | ------ | ---| --- | --- |
| orgId | Unique identifier for an organization. Example `12345@AdobeOrg` | path | string | true |
| userString | For Type 1, Type 2 and Type 3 _email-federated_ users this should be the full email address including domain. For Type 3 _username-federated_ users, this should be the username. In both cases the parameter is case-insensitive. | path | string | true |
| x-api-key | API key generated as part of a [Service Account integration](https://adobe-apiplatform.github.io/umapi-documentation/en/getstarted.html). | header | string | true |
| domain | Optional parameter but highly recommended including for all user types. For Type 1 users this would be `AdobeID`. For Type 2 and Type 3 _email-federated_ users the domain will either match the email domain or, in the case of multi-domain federations, have any other domain for that directory. For Type 3 _username-federated_ users the value must be a claimed domain which contains the user's account | query | string | false |
| Authorization | Contains the OAuth token generated from the JWT exchange and always begins with the letters `ey'. The word `Bearer` must precede the token. `'Authorization: Bearer ey...'` | header | string | true |
| Content-type | Used to specify the content type of the request data. Should be `application/json` | header | string | false |
| X-Request-Id | Arbitrary string which will be returned in response headers. This is to help assist in identifying the corresponding response to a request. | header | string | false |
___
## Responses

__Content-Type:__ _application/json_

### 200 OK
The response body contains the requested user data in JSON format including any of the user's group membership and admin roles. Fields can be missing if values were never supplied or are not applicable for a particular account type.

[Identity Types](https://helpx.adobe.com/enterprise/help/identity.html) explains the different account types available.

#### Examples
Response for an Adobe ID (Type 1) with System Administrator role:
```json
{
  "result": "success",
  "user": {
    "email": "jdoe@my-domain.com",
    "status": "active",
    "username": "jdoe@my-domain.com",
    "domain": "my-domain.com",
    "firstname": "John",
    "lastname": "Doe",
    "country": "US",
    "type": "adobeID",
    "adminRoles": [
      "org"
    ]
  }
}
```
Enterprise User (Type 2) with membership to 2 user-groups but no administrative roles. If the fields are not populated e.g. `firstname`/`lastname` in this example, then they will be excluded from the response.
```json
{
  "result": "success",
  "user": {
    "email": "jdoe@my-domain.com",
    "status": "active",
    "groups": [
      "UserGroup1",
      "UserGroup2"
    ],
    "username": "jdoe@my-domain.com",
    "domain": "my-domain.com",
    "country": "JP",
    "type": "enterpriseID"
  }
}
```
Federated User (Type 3) with no memberships or administrative roles:
```json
{
  "result": "success",
  "user": {
    "email": "jdoe@my-domain.com",
    "status": "active",
    "username": "johndoe",
    "domain": "my-domain.com",
    "firstname": "John",
    "lastname": "Doe",
    "country": "US",
    "type": "federatedID"
  }
}
```
#### Schema Properties

__message:__ _string_  
Only returned if initial validation of the request fails. It is not populated when a 200 status is returned.

```json
{
  "result": "error.organization.invalid_id",
  "message": "Bad organization Id"
}
```

__result:__ _string_, possible values: `{ "success", "error", "error.apikey.invalid", "error.user.email.invalid", "error.api.user.not.parent.org", "error.organization.invalid_id" }`  
The status of the request. This property can be used to manage error handling as the value will either be `success` or a corresponding error.

__user:__  
Represents a _User_ object. Properties that are not populated __will not__ be returned in the response. Some properties are not applicable for particular account types.

&nbsp;&nbsp;&nbsp;&nbsp;**adminRoles:** _string[]_  
&nbsp;&nbsp;&nbsp;&nbsp;The list of groups that the user holds an administrative role.

&nbsp;&nbsp;&nbsp;&nbsp;__country:__ _string_  
&nbsp;&nbsp;&nbsp;&nbsp;A valid ISO 2-character country code for a country in which Adobe does business.

&nbsp;&nbsp;&nbsp;&nbsp;__domain:__ _string_  
&nbsp;&nbsp;&nbsp;&nbsp;The user's domain (applicable for enterprise and federated users).

&nbsp;&nbsp;&nbsp;&nbsp;__email:__ _string_

&nbsp;&nbsp;&nbsp;&nbsp;__firstname:__ _string_

&nbsp;&nbsp;&nbsp;&nbsp;__groups:__ _string[]_  
&nbsp;&nbsp;&nbsp;&nbsp;The list of groups that the user is a current member of including user-groups and product configurations.

&nbsp;&nbsp;&nbsp;&nbsp;__id:__ _string_

&nbsp;&nbsp;&nbsp;&nbsp;__lastname:__ _string_

&nbsp;&nbsp;&nbsp;&nbsp;__status:__ _string_, possible values:`{ "active", "disabled", "locked", "removed" }`
&nbsp;&nbsp;&nbsp;&nbsp;The current status of the user.

&nbsp;&nbsp;&nbsp;&nbsp;__type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`  
&nbsp;&nbsp;&nbsp;&nbsp;The user type. See [Identity Types](https://helpx.adobe.com/enterprise/help/identity.html) for more information.

&nbsp;&nbsp;&nbsp;&nbsp;__username:__ _string_   
&nbsp;&nbsp;&nbsp;&nbsp;The user's username (applicable for enterprise and federated users).

#### Schema Model

```json
{
  "message": "string",
  "result": "string",
  "user": {
    "adminRoles": [
      "string"
    ],
    "country": "string",
    "domain": "string",
    "email": "string",
    "firstname": "string",
    "groups": [
      "string"
    ],
    "id": "string",
    "lastname": "string",
    "status": "string",
    "type": "string",
    "username": "string"
  }
}
```

### 400 Bad Request
Some parameters of the request were not understood by the server or the [Service Account Integration](https://adobe-apiplatform.github.io/umapi-documentation/en/getstarted.html) certificate has expired.

### 401 Unauthorized
Possible causes are:
- Invalid or expired token.
- Invalid Organization.

### 403 Forbidden
Possible causes are:
- Missing API key.
- The organization is currently migrating. Either from DMA or to One Console.

### 404 Not Found
The user was not found in the given organization.
