### <a name="{{ include.anchor }}" class="api-ref-subtitle">400 Bad Request</a>
Some parameters of the request were not understood by the server or the [Service Account Integration](../getstarted.html) certificate has expired.

{% if include.object == "user-group" %}
Possible cause:
- Group name already exists

```
> POST /v2/usermanagement/users/092DE2D65617B9967F000101@AdobeOrg/user-groups HTTP/1.1
< HTTP/1.1 400 Bad request
< Canonical-Resource: /v2/usermanagement/users/{orgId}/{page}/{groupName}
{"errorMessage":"DUPLICATE_GROUP_NAME","errorCode":"DUPLICATE_GROUP_NAME"}
```
{% endif %}
