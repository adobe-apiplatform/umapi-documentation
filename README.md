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

# Directory structure

From a engineering perspective, we are interested in the following files:
* 'en/api/': contains all the API reference documentation
* 'assets/css/style.scss': global stylesheet for the site
* '_includes/apiRef': contains all the documentation partials used inside the reference docs such as:
	* common response errors (e.g. Not Found, Forbidden, Unauthorized)
	* common request parameter descriptions (e.g. OrgId, X-Api-Key, X-Request-Id)


