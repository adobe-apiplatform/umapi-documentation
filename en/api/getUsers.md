---
title: Manage Users
layout: default
nav_link: Get all Users in an Organization
nav_order: 433
nav_level: 3
lang: en
---

# <a name="getUsers" class="api-ref-title">Get Users</a>
UMAPI has two APIs for retrieving a list of users. The selection of which API to use can be determined by aesthetic preference and required filtering of results:
* [GET /v2/usermanagement/users/{orgId}/{page}](getUsersWithPage.html)
  * Return a list of paginated users using a path parameter.
  * Filter users by domain.
  * Return a list of all the _direct only_ memberships for each user.
  * Return a list of all the _indirect_ memberships for each user.
* [GET /v2/usermanagement/{orgId}/users](getUsersREST.html)
  * Return a list of paginated users using a query parameter.
  * Return a list of all the _direct only_ memberships for each user.
  * Return a list of all the _indirect_ memberships for each user.