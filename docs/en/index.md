---
layout: page
title: User Management API Documentation
nav_link: UMAPI
nav_level: 1
nav_order: 15
lang: en
---

Welcome to the documentation center for User Management APIs from Adobe.  

<h2>News</h2>
<div class="isa_info">
<p><strong>July 23, 2025</strong>: We've been made aware that some customers are receiving group names with a mysterious suffix, such as <code>provisioning</code>. Since these groups or profiles with these names don't exist in Admin Console (they were a historic construct from a previous iteration of the Adobe platform), we will ensure that we fully filter out these mystery group names. APIs that return lists of group names will be changed to return <strong>only</strong> user group and product profile names that really exist in the org.</p>
<p>As a best practice, it is recommended to avoid any logic that expects fixed names.</p>
<p>This change will come into effect on <em><strong>August 26, 2025</strong></em>.</p>
<hr class="api-ref-rule">
<p><strong>May 22, 2025</strong>: With the introduction of the <a href="https://helpx.adobe.com/uk/enterprise/using/admin-roles.html#enterprise">Contract Admin role</a> in 2024, we've been made aware that some customers are not receiving a <code>type</code> value from the <a href="https://adobe-apiplatform.github.io/umapi-documentation/en/api/group.html">Get User Groups and Product Profiles</a> API. To help with consistency, we'll ensure that this scenario results in a type of <code>CONTRACT_ADMIN_GROUP</code> and will enhance the response with a <code>contractName</code> field as below:</p>
<pre>
    {
      "groupId": 555555555,
      "groupName": "BCDEFA3F5A9DB8F0345B_CONTRACT_GROUP",
      "adminGroupName": "_admin_BCDEFA3F5A9DB8F0345B_CONTRACT_GROUP",
      "type": "CONTRACT_ADMIN_GROUP",
      "contractName": "ETLA - BCDEFA3F5A9DB8F0345B",
      "memberCount": 1
    }
</pre>
<p>This change will come into effect on <em><strong>June 3, 2025</strong></em>.</p>
<hr class="api-ref-rule">
<p><strong>May 9, 2025</strong>: With the introduction of Single App Edition 4, we've been made aware that some customers have both Single App and Single App Edition 4. To help distinguish groups for each Single App using the same infix structure introduced in May 2023, the `productName` field for the profile will be adjusted to return the "parent" product name, as in the below examples:</p>
<ul>
	<li>If the parent product is <em>Single App - Enterprise</em>, you will see <code>Photoshop (&lt;keyword1,Single App - Enterprise,keyword2&gt;)</code></li>
	<li>If the parent product is <em>Single App - Edition 4</em>, you will see <code>Photoshop (&lt;keyword1,Single App - Edition 4,keyword2&gt;)</code></li>
</ul>
<p>If you rely on the name of the "product admin group", you will also see a change here.</p>
<p>This change will come into effect on <em><strong>June 10, 2025</strong></em>.</p>
<hr class="api-ref-rule">
<p><strong>April 15, 2025</strong>: As of <em><strong>October 16, 2025</strong></em>, UMAPI will no longer return "tags" information as documented for the following APIs:</p>
	<ul>
		<li><a href="api/getUser.html">Get User Information</a></li>
		<li><a href="api/getUsersWithPage.html">Get Users in Organization</a></li>
		<li><a href="api/getUsersByGroup.html">Get Users by Group</a></li>
	</ul>
<p>Note that this data is likely to become stale over the coming months as the attribute is deprecated internally. If you are currently using this information, please get in touch with the developer support team to let us know your use case. Note that as this change is due to the data being retired from the Adobe platform, UMAPI will not be able to offer extensions to this time frame.</p>
<hr class="api-ref-rule">
<p><strong>July 22, 2024</strong>: To provide peace of mind for API integrations, all APIs provided by UMAPI, even those marked as deprecated will continue to be supported for the foreseeable future.</p>
<p>If it becomes apparent that any API, deprecated or otherwise, needs to be retired from service or needs updated with a breaking change, Adobe will provide at least 6 (six) months notice of the change, via UMAPI documentation (this site) and via Developer Console banners.</p>
<p>We will also endeavour to provide 4 weeks notice of any new fields that are being added to responses in order to give time to prepare. As ever, guidance is to ignore any unrecognised or unknown fields in the UMAPI response. Unless it is documented, it should not be relied upon.</p>
<p>Developer support will also work to make customers aware of the upcoming removal of APIs during their regular engagement process.
</p>
<hr class="api-ref-rule">
<p>From Jan 16th 2024, a new query parameter <code>excludeGroups</code> will be available in <a href="api/getUsersByGroup.html">Get Users by Group</a> to exclude the return of other group membership information for each user.</p>
<p>Further information and examples can be found within the API documentation.</p>
<p>This does not impact existing clients.</p>
<hr class="api-ref-rule">
<p>From July 25th 2023, a new tags property will be returned as part of a user's response in the following APIs:</p>
	<ul>
		<li><a href="api/getUser.html">Get User Information</a></li>
		<li><a href="api/getUsersWithPage.html">Get Users in Organization</a></li>
		<li><a href="api/getUsersByGroup.html">Get Users by Group</a></li>
	</ul>
<p>Further information can be found within the API documentation. If you ignore unknown fields then you should expect no impact from this change.</p>
<hr class="api-ref-rule">
<p>On May 9th, 2023, the <code>productName</code> will be updated to include a new structure to help distinguish multiple products with the same name. An example of the structure is <code>&lt;Product Name&gt; (&lt;a list of keywords&gt;)</code>. For ETLA customers with a <a href="https://helpx.adobe.com/uk/enterprise/using/single-app.html">Single App plan</a> (the plan which enables you to choose any one app from a set of available Creative Cloud applications) you may be returned a structure like <code>Photoshop (&lt;keyword1,Single App,keyword2&gt;)</code> where keyword1 and keyword2 could be optional.</p><p>As a result, any application directly accessing the User Management API which includes logic <strong>dependent on fixed product names</strong> will need to be updated. If you have not included fixed product names in the code, then this will not impact your connection to the User Management API. If you use the User Sync Tool, you should see no impact.</p>
<p>If you rely on the name of the “product admin group” (e.g., <code>_product_admin_&lt;product name&gt;</code>) you will also be impacted and have to update your scripts.</p>
<p>You should avoid any logic that expects fixed group names as these are liable to change without notice. We recommend using the Get Groups and Profiles API to fetch the latest group information.</p>
<hr class="api-ref-rule">
<p>Since May 6th, 2023, User Management API supports OAuth Server-to-Server (S2S) workflows; The JWT one is deprecated and will stop working from the 27th of January 2025. Existing integrations based on this authorization scheme will continue to work as usual until this date. Please migrate your project to use OAuth S2S before 2025. 
<p>For User Sync Tool users, please wait for the v2.9.0 release before migrating to OAuth Server-to-Server.</p>
<hr class="api-ref-rule">
<p>On August 8th, 2022, Document Cloud product names will remove the "DC" suffix. For example, "Acrobat Pro DC" will be renamed “Acrobat Pro".</p>
<p>As a result, any application directly accessing the User Management API which include logic <strong>dependent on the product name</strong> will need to be updated. If you have not included the product name in the code, then this will not impact your connection to the User Management API. If you use the User Sync Tool, you should see no impact.</p>
<p>Note: the term "DC" included in the name of a Product Profile <em>will not change</em>. If you rely on the name of the “product admin group” (e.g., <code>_admin_&lt;product name&gt;</code>) you may be impacted and have to update your scripts.</p>
<p>As a best practice, it is recommended to avoid any logic that expects fixed product names.</p>
<hr class="api-ref-rule">
<p>Since October 2021, Adobe has added controls to check the running frequency of each UMAPI client instance to prevent running syncs more frequently than the recommended timing of no more than once every 2 hours. Running the calls more frequently can start a new session prior to the completion of the previous session, resulting in syncing delays. When the access limit is reached, further calls fail with the error message ‘429 Too Many Requests’ and a Retry-After header containing the delay required before the next call can be made. Please refer to the _Throttling_ section of each API to determine its limitations.</p>
<hr class="api-ref-rule">
<p>Starting from 20th July 2021, there is an update when retrieving groups for ETLA customers with a Single App plan. When applicable, instead of returning _Single App_ in the <code>productName</code> field it will now be populated with the corresponding product name e.g. _Photoshop_.</p>
<p>As a result, any application directly accessing the User Management API which includes logic <strong>dependent on the _Single App_ product name</strong> will need to be updated. If you have not included the product name in the code, then this will not impact your connection to the User Management API. If you use the User Sync Tool, you should see no impact.</p>
<p>As a best practice, it is recommended to avoid any logic that expects fixed product names.</p>
<hr class="api-ref-rule">
<p>Since 27th April 2021, the page size for APIs relating to the retrieval of users has been increased from 1000 to 2000. No changes are required by existing clients.</p>
<hr class="api-ref-rule">
<p>Starting in February 2021, Adobe will add controls to check the running frequency of each User Sync Tool instance to prevent running the tool more frequently than the recommended timing of no more than once every 2 hours. Running the calls more frequently can start a new session prior to the completion of the previous session, resulting in syncing delays. When the access limit is reached, further calls fail with the error message ‘429 Too Many Requests’ and a Retry-After header containing the delay required before the next call can be made. Please refer to the _Throttling_ section of each API to determine its limitations and, if you are leveraging the User Sync Tool, please check their Deployment Best Practices section for scheduling recommendations.</p>
<hr class="api-ref-rule">
<p>Since June 8th 2020, the page size for APIs relating to the retrieval of users has been increased from 400 to 1000. No changes are required by existing clients.</p>
<hr class="api-ref-rule">
<p>Starting March 10th 2020, new property <code>groupId</code> will be returned as part of the response for retrieving groups and products. Clients are not impacted by this change.</p>
<hr class="api-ref-rule">
<p>Since February 11th 2020, the page size for APIs relating to the retrieval of groups has been increased from 200 to 400. No changes are required by existing clients.</p>
<hr class="api-ref-rule">
<p>Starting August 8th 2019, a change is applied to align with the multiple domains per directory model and tightening the security of the <strong>create</strong> and <strong>update</strong> APIs.</p>
<p>As a result, any application using the <strong>create</strong> or <strong>update</strong> API statements using domains for which there's no claim in Admin Console, will start failing.</p>
<hr class="api-ref-rule">
<p>On April 2nd, 2019, Creative Cloud product names will remove the “CC”. For example, “Photoshop CC” will be renamed “Photoshop”.</p>
<p>As a result, any application directly accessing the User Management API which include logic <strong>dependent on the product name</strong> will need to be updated. If you have not included the product name in the code, then this will not impact your connection to the User Management API. If you use the User Sync Tool, you should see no impact.</p>
<p>Note: the term “CC” included in the name of a Product Profile <em>will not change</em>. If you rely on the name of the “product admin group” (e.g., <code>_admin_&lt;product name&gt;</code>) you may be impacted and have to update your scripts.</p>
<p>As a best practice, it is recommended to avoid any logic that expects fixed product names.</p>
</div>



[Getting Started with User Management](getstarted.md)

[User Management API Overview](API_introduction.md)

[User Management API Reference](RefOverview.md)

[User Management Walkthrough](samples/index.md)
