
{% if include.keys != nil %}
{% assign keys = include.keys | split: "," %}
{% endif %}

<section>
<h3 class="no_toc">References</h3>
<ul class="bibliography">

{% if include.keys != nil %}
{% assign keys = include.keys | split: "," %}
{% endif %}
<section>
<h3 class="no_toc">References</h3>
<ul class="bibliography">
---
layout: page
title: Thesis bibliography 
in-menu: no
---
{% include bibliography.html %}
</ul>
</section>

</ul>
</section>
