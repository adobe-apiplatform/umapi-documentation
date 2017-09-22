### <a name="{{ include.anchor }}" class="api-ref-subtitle">404 Not Found</a>
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
< HTTP/1.1 404 Not Found
< Canonical-Resource: /v2/usermanagement/users/{orgId}/{page}/{groupName}
{"lastPage":false,"result":"error.group.not_found","message":"Not found: Group 1234"}
```
{% endif %}
{% if include.object == "plc" %}
```
< HTTP/1.1 404 Not Found
< Canonical-Resource: /v2/usermanagement/{orgId}/products/{productId}/configurations/{id}
< Content-Type: application/json
< X-Request-Id: iB93be6zWzNg19TljWt2IvZCxSWHis5l
< Connection: keep-alive
{"errorMessage":"PLC_NOT_FOUND","errorCode":"PLC_NOT_FOUND"}
```
{% endif %}