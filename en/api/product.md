---
title: Access Product Information
layout: default
nav_link: Access Product Information
nav_order: 443
nav_level: 3
lang: en
---

The following set of APIs allow users to retrieve information about their organization's [products](glossary.html#product).

_Product_ access for individual users is controlled through membership in [user-groups](glossary.html#usergroup) and [product configurations](glossary.html#plc). You cannot create these groups through the User Management API. Before you can manage product access for users, you must create and name user groups and product configurations using the [Admin Console](glossary.html#adminconsole).

A product can have more than one license configuration associated with it, to allow different access privileges for different sets of users. For example, if your organization uses Adobe Document Cloud Pro, you could have one product configuration that blocks access to related services and another that only allows access to E-sign services.

Both individual users and user groups can be members of a product configuration. An individual user can gain access to a particular product directly, or through user-group membership. Within a product configuration, member users can be assigned an admin role.

You can manage access for individual users through the [Action API](ActionsRef.html) endpoint or manage access rights through the individual endpoints for products and product configurations that are listed below.