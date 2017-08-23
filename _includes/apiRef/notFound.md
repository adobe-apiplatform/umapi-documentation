### 404 Not Found
The {{ include.object }} was not found in the given organization.

{% if include.object == "user" %}
```
< HTTP/1.1 404 Not Found
< Canonical-Resource: /v2/usermanagement/organizations/{orgId}/users/{userstring:.*}
< Content-Type: application/json
< X-Request-Id: user-assigned-request-id
< Connection: keep-alive
{"result":"error.user.not_found","message":"User not found email@email.com"}
```
{% endif %}
{% if include.object == "group" %}
```
> GET /v2/usermanagement/users/092DE2D65617B9967F000101@AdobeOrg/0/Group 1234 HTTP/1.1
> postman-token: c0a973fe-0267-9d76-779a-270aeb8ca39c
< HTTP/1.1 404 Not Found
< Canonical-Resource: /v2/usermanagement/users/{orgId}/{page}/{groupName}
{"lastPage":false,"result":"error.group.not_found","message":"Not found: Group 1234"}
```
{% endif %}