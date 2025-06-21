---
layout: default
title: "Index"
---

<h1>My Collection</h1>

<!-- In-Page Navigation Menu -->
<nav class="in-page-nav">
  <ul>
    {% for section in site.data.index_sections.sections %}
      <li><a href="#{{ section.id }}">{{ section.title }}</a></li>
    {% endfor %}
  </ul>
</nav>

<div class="index-scroll-container">
  {% for section in site.data.index_sections.sections %}
    <section id="{{ section.id }}">
      <h3>{{ section.title }}</h3>
      <div class="button-container">
        {% for button in section.buttons %}
          <a class="button" href="{{ button.url }}" target="_blank">{{ button.text }}</a>
        {% endfor %}
      </div>
    </section>
  {% endfor %}
</div>
_sections