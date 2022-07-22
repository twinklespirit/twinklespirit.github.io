---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_programmers_sql
# 제목 설정 (사용 언어로 작성)
title: 프로그래머스 (SQL) 오답정리
# 카테고리 설정 (1개)
category: 개인공부
# 태그 설정 ([태그1, 태그2, ...])
tags: [자료구조, 알고리즘] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/179664690-fe40a0ea-160d-4e74-a082-77f030679c8a.png)" 
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-19 13:00:00 +0900

################################### 게시 글 기타 정보 설정 ###################################
# 댓글 비활성화 여부
comments_disable: false

# Mathjax 사용
use_math: true

# image_viewer_posts = false 혹은 image_lazy_loader_posts = false인 경우에만 사용
#image_viewer_on: true
#image_lazy_loader_on: true

# 사이트에서 검색하기 혹은 검색 엔진 제외 설정 
#on_site_search_exclude: true
#search_engine_exclude: true

# 페이지 비활성화 설정 (혹은 삭제하면 됨)
#published: false

##########################################################################################
# 👇 본격적으로 글을 작성하면 됩니다. 

---
<!-- outline-start -->


<!-- outline-end -->

~~~sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) "count"
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY FIELD(ANIMAL_TYPE, "Cat", "Dog")
~~~

~~~sql
SELECT HOUR(DATETIME) "HOUR", COUNT(DATETIME) "COUNT"
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) < 20 AND HOUR(DATETIME) > 8
GROUP BY HOUR
ORDER BY HOUR;
~~~

