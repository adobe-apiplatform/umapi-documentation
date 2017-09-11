### <a name="{{ include.anchor }}" class="api-ref-subtitle">401 Unauthorized</a>
Possible causes are:
- Invalid or expired token.
- Invalid Organization.

```
< HTTP/1.1 401 Unauthorized
< Content-Type: */*
< Date: Thu, 22 Jun 2017 09:47:04 GMT
< WWW-Authenticate: Bearer realm="JIL", error="invalid_token", error_description="The access token is invalid"
< X-Request-Id: user-assigned-request-id
< Content-Length: 0
< Connection: keep-alive
```
