---
layout: page
navigation_title: Tags
title: Article Tags
permalink: /tags/
regenerate: true
---

{% assign tags_list = site.tags | sort %}
<ul>
  {% for tag in tags_list %}
    <li><a href="/tags#{{ tag[0] | replace: ' ', '-' }}" class='list-group-item'>
      {{ tag[0] }}
    </a></li>
  {% endfor %}
</ul>

{% for tag in tags_list %}

<h1 class='event-time-heading' id="{{ tag[0] | replace: ' ', '-' }}">{{ tag[0] }}</h1>
<div class="clearfix">                                               
{% assign pages_list = tag[1] %}
{% for post in pages_list %}
<a href="{{ post.url | prepend: site.baseurl }}">
{% if post.cover %}
<div class="event-square" style="background-image:url({{post.cover | replace_first: '/images', '/images/thumbnails' }});">
{% else %}
<div class="event-square" style="background-image:url(/images/wedding-robots-banner.jpg);">
{% endif %}
<h2>{{ post.title }} <span>{{ post.date | date: "%b %-d, %Y" }}</span></h2>
<div class='event-square-overlay'></div>
</div>
</a>
{% endfor %}
</div>

{% endfor %}

