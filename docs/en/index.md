---
layout: page
title: User Management API Documentation
nav_link: UMAPI
nav_level: 1
nav_order: 15
lang: en
---

Welcome to the documentation center for User Management APIs from Adobe.  

News:  
<div class="isa_info">
<p>On August 8th, 2022, Document Cloud product names will remove the "DC" suffix. For example, "Acrobat Pro DC" will be renamed “Acrobat Pro".</p>
<p>As a result, any application directly accessing the User Management API which include logic <strong>dependent on the product name</strong> will need to be updated. If you have not included the product name in the code, then this will not impact your connection to the User Management API. If you use the User Sync Tool, you should see no impact.</p>
<p>Note: the term "DC" included in the name of a Product Profile <em>will not change</em>. If you rely on the name of the “product admin group” (e.g., <code>_admin_&lt;product name&gt;</code>) you may be impacted and have to update your scripts.</p>
<p>As a best practice, it is recommended to avoid any logic that expects fixed product names.</p>
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
