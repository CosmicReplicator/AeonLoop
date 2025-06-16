---
layout: default          # whatever your front-matter already uses
title:  "AeonLoop"
---

# AeonLoop Project

Intro text … your hero image … whatever.

## Papers                    <!-- ⬅ keeps the same heading -->

<ul>
{% assign papers = site.pages
                   | where_exp: "p", "p.url contains '/papers/'" %}
{% assign papers = papers | sort: "nav_order" | sort: "title" %}

{% for p in papers %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

## Other sections
…
