---
layout: links
# multilingual page pair id, this must pair with translations of this page. (This name must be unique)
lng_pair: id_links

# publish date (used for seo)
# if not specified, site.time will be used.
#date: 2022-03-03 12:32:00 +0000

# for override items in _data/lang/[language].yml
#title: My title
#button_name: "My button"
# for override side_and_top_nav_buttons in _data/conf/main.yml
#icon: "fa fa-bath"

# seo
# if not specified, date will be used.
#meta_modify_date: 2022-03-03 12:32:00 +0000
# check the meta_common_description in _data/lang/[language].yml
#meta_description: ""

# optional
# if you enabled image_viewer_posts you don't need to enable this. This is only if image_viewer_posts = false
#image_viewer_on: true
# if you enabled image_lazy_loader_posts you don't need to enable this. This is only if image_lazy_loader_posts = false
#image_lazy_loader_on: true
# exclude from on site search
#on_site_search_exclude: true
# exclude from search engines
#search_engine_exclude: true
# to disable this page, simply set published: false or delete this file
#published: false


# you can always move this content to _data/content/ folder
# just create new file at _data/content/links/[language].yml and move content below.
###########################################################
#                Links Page Data
###########################################################
page_data:
page_data:
  main:
    header: 참고 사이트
    info: 게시 글 작성에 참고한 사이트 정보입니다.

  # 카테고리 순서를 바꿀 수 있음 (List 순서는 변경할 필요가 없음)
  category:
    - title: 카테고리1
      type: id_카테고리1
      color: black
    - title: 카테고리2
      type: id_카테고리2
      color: black

  list:
    -
    - type: id_카테고리2
      title: Google
      url: https://www.google.com
      info: 구글 사이트입니다.

    - type: id_카테고리1
      title: 네이버
      url: https://www.naver.com
      info: 네이버 사이트입니다.
    - type: id_카테고리1
      title: 다음
      url: https://www.daum.net/
      info: 다음 사이트입니다.
---
