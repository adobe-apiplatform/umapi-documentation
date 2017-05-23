---
title: Throttling
layout: page
nav_link: Throttling
nav_order: 35
nav_level: 2
lang: en
---

# Data Access Limits

To protect the availability of the Adobe back-end user identity systems, the User Management API imposes limits on client access to the data. Limits apply to the number of calls that an individual client can make within a time interval, and global limits apply to access by all clients within the time period.

Specific limits may change over time, but these are general guidelines.

| Client calls | Per client maximum | Global maximum (all clients) | 
| --- | --- | --- |
| /action | 10 requests per minute | 100 requests per minute |
| /users | 25 requests per minute | 100 requests per minute |
| /groups | 5 requests per minute | 50 requests per minute |

When the access limit is reached, further calls fail with one of the following HTTP error status responses:

* **429 Too Many Requests** – You are being rate limited, delay before retry
* **503 Service Unavailable** – Global limits have been reached, delay before retry

Because of the global limits, and because the specific limits may change, you cannot simply limit the rate at which you make your own calls. You must handle rate-limit errors by retrying the failed calls.  We recommend a technique for handling such errors called "exponential backoff retry".

## Handling error responses

When you retry a failed request, the retry can also fail, and can fall back into the retry loop, adding to the system overload. The exponential backoff retry method increases the period between retries, so that the client makes fewer calls while the system is overloaded.

To implement an exponential backoff method, you increase the retry interval with each failed request. You should retry sending the request after a certain number of seconds, and increase that interval by a random amount with each attempt. For example, you can double the retry period each time, or escalate it by a power of 2, and then add a small random delay between failures.

A small random delay, known as "jitter," prevents the "herd effect" that can occur if many clients attempt to reconnect to a recovering system at the same time. Without jitter, all of the retries could occur after 20 seconds, then 40 seconds, and so on. With the jitter, different retries occur at slightly different intervals. This allows the system to recover without further overloading it.

For an example of how to implement this error-handling method, see "Retrying Requests" in the [User Management Walkthrough](samples/index.html).
