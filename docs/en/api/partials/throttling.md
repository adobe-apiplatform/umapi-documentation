To protect the availability of the Adobe back-end user identity systems, the User Management API imposes limits on client access to the data. Limits apply to the number of calls that an individual client can make within a time interval, and global limits apply to access by all clients within the time period. For this API the throttling limits are as follows:

- Maximum calls per client: **{{ include.client }} requests per a minute**
- Maximum calls for the application: **{{ include.global }} requests per a minute**

When the client or global access limit is reached, further calls fail with HTTP error status **429 Too Many Requests**. The **Retry-After** header is included in the 429 response, and provides the minimum amount of time that the client should wait until retrying. See [RFC 7231](https://tools.ietf.org/html/rfc7231#section-7.1.3) for full information.

**Important:** The page index 0 (first page) of GET All Users / GET All Groups from Organisation API call is throttled separately. Calling it too often will trigger the frequency throttling  with high delay timeouts (>2000 sec). All subsequent API calls will be blocked during this time.
The recommended frequency is calling GET all users in the Organisation, page index 0, at most once every two hours.

For User Sync Tool instances the running frequency should be set to no more than once every two hours.

The following sample shows a 429 response with the Retry-After header detailing the number of seconds to wait before retry:

```
========================= RESPONSE =========================
Status code: 429
-------------------------- header --------------------------
Content-Type: application/json
Date: Fri, 19 Jan 2018 10:31:43 GMT
Retry-After: 38
Server: APIP
X-Request-Id: iEUtsLiFgj3R4xsbirAyZlMyaxRTo8Xo
Content-Length: 54
Connection: keep-alive
--------------------------- body ---------------------------
{
  "error_code" : "429050",
  "message" : "Too many requests"
}
============================================================
```

Because of the global limits, and because the specific limits may change, you cannot simply limit the rate at which you make your own calls. You **must** handle rate-limit errors by retrying the failed calls. We recommend an _exponential backoff retry_ technique for handling such errors.

### Handling error responses

When you retry a failed request, the retry can also fail, and can fall back into the retry loop, adding to the system overload. The exponential backoff retry method increases the period between retries, so that the client makes fewer calls while the system is overloaded.

To implement an exponential backoff method, you increase the retry interval with each failed request. You should retry sending the request after a certain number of seconds, and increase that interval by a random amount with each attempt. For example, you can double the retry period each time, or escalate it by a power of 2, and then add a small random delay between failures.

A small random delay, known as "jitter," prevents the "herd effect" that can occur if many clients attempt to reconnect to a recovering system at the same time. Without jitter, all of the retries could occur after 20 seconds, then 40 seconds, and so on. With the jitter, different retries occur at slightly different intervals. This allows the system to recover without further overloading it.

For an example of how to implement this error-handling method, see "Retrying Requests" in the [User Management Walkthrough](../samples/index.html).
