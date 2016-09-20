---
layout: blazy
cover: '/images/wedding-robots-banner.jpg'
permalink: /archive/
regenerate: true
---

<div class="home">

    <div class="clearfix">

	   <h1 class="event-time-heading fix-top">Events Archive</h1>

      {% for post in site.posts %}{% capture cache %}

        {% if post.repeat_every %}
            {% continue %}
        {% endif %}

        {% assign startYMD = post.date | date: '%b %-d, %Y' %}
        {% assign endYMD = post.endDate | date: '%b %-d, %Y' %}

        {% endcapture %}{% assign cache = nil %}
          <a href="{{ post.url | prepend: site.baseurl }}">
            {% if post.cover %}
            <div class="event-square" style="background-image:url({{post.cover | replace_first: '/images', '/images/thumbnails' }});">
            {% else %}
            <div class="event-square" style="background-image:url(/images/wedding-robots-banner.jpg);">
            {% endif %}
              <h2>{{ post.title }} <span>{{ startYMD }}{%if startYMD != endYMD %} - {{ endYMD }}{% endif %}</span></h2>
               <div class='event-square-overlay'></div>
            </div>
          </a>
      {% endfor %}
    </div>

</div>
