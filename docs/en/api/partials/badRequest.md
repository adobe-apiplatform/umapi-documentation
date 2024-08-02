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

- Attempting to modify a readonly group e.g. update the group name

```
> v2/usermanagement/action/56EB197B663A09470A494111@AdobeOrg HTTP/1.1
> [
>   {
>     "usergroup": "UMAPI Test",
>     "do": [
>       {
>         "updateUserGroup": {
>           "name": "UMAPI Test Updated"
>         }
>       }
>     ]
>   }
> ]
< Canonical-Resource: /v2/usermanagement/action/{orgId}
< {
<   "completed": 0,
<   "notCompleted": 1,
<   "completedInTestMode": 0,
<   "result": "error",
<   "errors": [
<     {
<       "index": 0,
<       "step": 0,
<       "message": "Usergroup is owned by another org and readonly: UMAPI Test",
<       "errorCode": "error.usergroup.readonly.update_not_allowed",
<       "user": "UMAPI Test"
<     }
<   ]
< }
```

- Attempting to add a user membership of a readonly group

```
> POST v2/usermanagement/action/56EB197B663A09470A494111@AdobeOrg HTTP/1.1
> [
>  {
>    "usergroup": "UMAPI Test",
>    "do": [
>      {
>        "add": {
>          "user": [
>            "test@user.com"
>          ]
>        }
>      }
>    ]
>  }
> ]
< Canonical-Resource: /v2/usermanagement/action/{orgId}
< {
<   "completed": 0,
<   "notCompleted": 1,
<   "completedInTestMode": 0,
<   "result": "error",
<   "errors": [
<     {
<       "index": 0,
<       "step": 0,
<       "message": "User cannot be added to group as owned by another org and readonly: UMAPI Test",
<       "errorCode": "error.usergroup.readonly.add_user_not_allowed",
<       "user": "UMAPI Test"
<     }
<   ]
< }
```

- Attempting to remove a user membership of a readonly group

```
> POST v2/usermanagement/action/56EB197B663A09470A494111@AdobeOrg HTTP/1.1
> [
>  {
>    "usergroup": "UMAPI Test",
>    "do": [
>      {
>        "remove": {
>          "user": [
>            "test@user.com"
>          ]
>        }
>      }
>    ]
>  }
> ]
< Canonical-Resource: /v2/usermanagement/action/{orgId}
< {
<   "completed": 0,
<   "notCompleted": 1,
<   "completedInTestMode": 0,
<   "result": "error",
<   "errors": [
<     {
<       "index": 0,
<       "step": 0,
<       "message": "User cannot be removed from group as owned by another org and readonly: UMAPI Test",
<       "errorCode": "error.usergroup.readonly.remove_user_not_allowed",
<       "user": "UMAPI Test"
<     }
<   ]
< }
```

- Attempting to remove a readonly group from the organization

```
> POST v2/usermanagement/action/56EB197B663A09470A494111@AdobeOrg HTTP/1.1
> [
>   {
>     "usergroup": "UMAPI Test",
>     "do": [
>       {
>         "deleteUserGroup": {}
>       }
>     ]
>   }
> ]
< Canonical-Resource: /v2/usermanagement/action/{orgId}
< {
<   "completed": 0,
<   "notCompleted": 1,
<   "completedInTestMode": 0,
<   "result": "error",
<   "errors": [
<     {
<       "index": 0,
<       "step": 0,
<       "message": "User group owned by another organization. Remove not allowed: UMAPI Test",
<       "errorCode": "error.usergroup.readonly.remove_not_allowed",
<       "user": "UMAPI Test"
<     }
<   ]
< }
```
{% endif %}
