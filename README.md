Current documentation: https://adobe-apiplatform.github.io/umapi-documentation/en/
Pending documentation: http://umsdk-docs.cmri.corp.adobe.com:4000

# Documentation review process

UMAPI documentation is generated using [Jekyll](https://jekyllrb.com). The workflow is to update documentation is as follows:
1. Include any documentation changes as part of the PR that is making the code change
2. Merge to RTT
3. Test feature as part of the stage deployment
4. Release to Production
5. Create a branch of `umsdk-doc-update` and add documentation changes
6. Review and Merge
7. Changes will be available after 1min at http://umsdk-docs.cmri.corp.adobe.com:4000

# Local setup

To test changes locally:
1. Set up [Jekyll](https://jekyllrb.com)
```
bundle install
gem install jekyll bundler
```
2. Pull down the latest of `RTT`
3. In `jil-core/resources/umsdk/docs/` directory, run `bundle exec jekyll serve`
4. Navigate to http://localhost:4000/en/
5. Make your changes and refresh the browser

# Running on Windows?

Try https://jekyllrb.com/docs/windows/

# Directory structure

From a engineering perspective, we are interested in the following files:
* 'en/api/': contains all the API reference documentation
* 'assets/css/style.scss': global stylesheet for the site
* '_includes/apiRef': contains all the documentation partials used inside the reference docs such as:
	* common response errors (e.g. Not Found, Forbidden, Unauthorized)
	* common request parameter descriptions (e.g. OrgId, X-Api-Key, X-Request-Id)


# Page Template

Use the following or an existing API as a template:

```
<a name="apiName" class="api-ref-title"></a>

METHOD {API PATH}

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#apiNameThrottle)

<a name="intro" class="api-ref-subtitle"></a>
description of the api

__Throttle Limits__: Maximum x requests per minute per a client. See [Throttling Limits](#apiNameThrottle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| X-Api-Key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
| request | body | true | JSON payload containing a series of commands. See [Request Body](#apiNameRequestBody) section for full details. |
{:.bordertablestyle}

<a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200apiName)
- [400: Bad Request](#400apiName)
- [401: Unauthorized](#401apiName)
- [403: Forbidden](#403apiName)
- [429: Too Many Requests](#apiNameThrottle)

<a name="200apiName" class="api-ref-subtitle">200 OK</a>

description of response

#### Headers

{% include apiRef/pagedResponseHeaders.md object="users" %}

#### Examples

supply json examples of the possible responses.

#### Schema Properties

add a description of each of the possible properties that can be returned.

#### Schema Model

{% include apiRef/badRequest.md anchor="400apiName" %}

{% include apiRef/unauthorized.md anchor="401apiName" %}

{% include apiRef/forbidden.md anchor="403apiName" %}

{% include apiRef/notFound.md object="user" anchor="404apiName" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>

add curl examples

## <a name="apiNameRequestBody" class="api-ref-subtitle">Request Body</a>

description

### <a name="apiNameRequestBodyProperties" class="api-ref-subtitle">Properties</a>
detail of the schema properties in the request body

### <a name="apiNameRequestBodyExamples" class="api-ref-subtitle">Examples</a>

### <a name="apiNameRequestBodySchema" class="api-ref-subtitle">Request Body Schema</a>

## Throttling

{% include apiRef/throttling.md client=10 global=100 %}

```

## Styles and Guidelines

* Use `api-ref-subtitle` class to remove hyperlinks from anchor links in all sub-headings.
* Use `api-ref-title` class to remove hyperlinks from API titles.
* Use `{:.bordertablestyle}` for styling tables.
* If you start to repeat yourself consider moving the text to a partial.
* Add a glossary item when required.