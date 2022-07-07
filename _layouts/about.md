---
# Mr. Green Jekyll Theme - v1.1.0 (https://github.com/MrGreensWorkshop/MrGreen-JekyllTheme)
# Copyright (c) 2022 Mr. Green's Workshop https://www.MrGreensWorkshop.com
# Licensed under MIT

layout: default
# About page
---
{%- include multi_lng/get-lng-by-url.liquid -%}
{%- assign lng = get_lng -%}
<!-- 블로그 정보/컨테이너-->
<div class="multipurpose-container about-container">
  <!-- 상단-->
  <div class="row about-main">
    <!-- 상단 좌측 컨테이너: 이미지-->
    <div class="col-md-3 about-img">
      <img src="{{ page.img }}" alt="">
    </div>
    <!-- 상단 우측 컨테이터: 글-->
    <div class="col-md-9 about-header">
      <h1 translate="no">{{ site.data.owner.brand }}</h1>
      <div class="meta-container">
        <!-- 이건 진짜.. 알고 싶지 않다.-->
        {{ site.data.lang[lng].about.sub_title }}
        <!-- \{  %   %  \}파일 경로 속성에 값이 있다면, 넣어라!-->
        {%- if site.data.lang[lng].about.sub_title %} 
          <p class="sub-title">
            {%- if site.data.conf.others.about.sub_title_icon %}<i class="{{ 'fa-fw ' }}{{ site.data.conf.others.about.sub_title_icon }}" aria-hidden="true"></i>{% endif -%}&nbsp;{{ about_title }}
          </p>
        <!-- 없다면, 넣어라!-->
        {% endif -%}
        {%- assign tmp_obj =  site.data.owner.contacts | where_exp: "item", "item.email != nil" | first -%}
        {%- assign email = tmp_obj['email'] -%}
        {%- if site.data.conf.others.about.show_email and email %}
          {%- assign _email = email | split: '@' %}
          <p class="email">
            <a href="javascript:void(0);" onclick="setAddress('{{ _email[0] }}', '{{ _email[1] }}');">
              {%- if site.data.conf.others.about.email_icon %}<i class="{{ 'fa-fw ' }}{{ site.data.conf.others.about.email_icon }}"></i>{% endif -%}
              &nbsp;{{ site.data.lang[lng].about.email_title }}
            </a>
          </p>
        {% endif -%}
        {%- if site.data.conf.others.about.show_contacts and site.data.owner.contacts.size > 0 %}
          {% include default/nav/contact-links.html -%}
        {% endif -%}
      </div>
    </div>
  </div>
  <div class="row about-divider">
    <hr>
  </div>
  <!-- 하단-->
  <div class="row">
    <div class="col-md-12">
      <div class="about-msg markdown-style">
        {{ content }}
      </div>
    </div>
  </div>
</div>
