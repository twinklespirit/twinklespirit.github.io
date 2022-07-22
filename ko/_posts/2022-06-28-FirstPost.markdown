---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_test1
# 제목 설정 (사용 언어로 작성)
title: 안녕하세요! 💫 드디어 해냈습니다..
# 카테고리 설정 (1개)
category: 기타
# 태그 설정 ([태그1, 태그2, ...])
tags: [기타, jeykll] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/179060515-34d353b5-f1df-4115-bd24-46ffedb529c3.png" 
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-06-28 18:47:35 +0900 

################################### 게시 글 기타 정보 설정 ###################################
# 댓글 비활성화 여부
comments_disable: false

# image_viewer_posts = false 혹은 image_lazy_loader_posts = false인 경우에만 사용
#image_viewer_on: true
#image_lazy_loader_on: true

# 사이트에서 검색하기 혹은 검색 엔진 제외 설정 
#on_site_search_exclude: true
#search_engine_exclude: true

# 페이지 비활성화 설정 (혹은 삭제하면 됨)
published: false

##########################################################################################
# 👇 본격적으로 글을 작성하면 됩니다. 

---
<!-- outline-start -->
[ 깃허브 블로그 ] - 1. Jeykll 사용하기

<!-- outline-end -->
## 서론
드디어 기술용 블로그를 위한 github.io를 개설하였습니다. 😃<br>
다국적 언어 블로그라는 명분으로 화딱지가 나게 해도 공들여 닦아줬네요. .yml, .html, .json, .md, liquid까지 난잡하고, 특히 이미지 경로가 어지러워요. 이런 건 직접 제품 생산 과정에 참여하고 싶은 Z세대 혹은 프론트엔드 개발자에게 추천합니다.  

**jeykll 사용방법**을 알아보겠습니다.
* Jekyll은 무엇일까요?
    * a static site generator
    * application written in ruby
    
## 1. 폴더 구조
매~우 꼼꼼하게 폴더를 뜯어보았습니다. 

### _config.yml
- 환경설정 정보를 보관
- 이곳에 명령어를 정의해두면 편리함

### _data
- 사이트에 사용할 데이터를 적절한 포맷으로 정리하는 폴더
- .yml, .json, .csv, .tsv 파일을 자동으로 읽어와서 site.data로 사용할 수 있게 함
    - 예) _data/twinkle.yml을 불러오려면, site.data.twinkle 

### _includes
- 재사용하기 위한 파일을 담는 폴더
- Liquid 태그를 이용하여 _layouts, _posts에 쉽게 삽입 가능
    - 예) **\{ % include file.ext % \}**을 이용하여 **_includes/file.ext** 파일에 담긴 코드 삽입

### _layouts
- 포스트를 포장할 때 사용
    - 예) **\{\{ content \}\}**를 이용하여 페이지에 **content**를 주입

### _posts
- 나의 컨텐츠라고 보면 됨
- 파일들의 명명규칙을 따라야 함
- 파일이름: YEAR-MONTH-DAY-title.MARKUP
    - 예) 2022-06-06-현충일.MARKUP

### _sass
- 사이트에서 사용할 스타일 정의
- main.sass는 main.css로 가공

### _site
- Jekyll이 변환 작업을 마친 뒤 생성된 사이트가 저장되는 경로
- .gitignore에 추가하는 걸 추천

### .jekyll-metacata
- Jekyll이 마지막 빌드 이후에 참고하는 파일
- 한번도 수정되지 않은 파일과 다음 빌드 때 어떤 파일을 다시 생성해야 하는지 판단하기 위함
- .gitignore에 추가하는 걸 추천

### index.html
- Jekyll의 변환 작업 대상 파일로, 위에서 언급하지 않은 모든 파일이 해당
- .html, .markdowm, .md, .textfile 등

## 2. Liquid
Jekyll를 좀 더 흥미롭게 만들어주는 도구  

### 2.1 오프젝트
- 컨텐츠를 어디에 출력할지 Liquid에게 알려줌
- \{\{ \}\}
    - 예) \{\{ page.title \}\} 페이지에 page.title의 변수 값을 출력합니다.

### 2.2 태그
- 템플릿의 논리 연산과 흐름을 제어
- \{ % % \}
    - 예) \{ % if page.show_sidebar % \} 
    ''' html
    <div clss=>

### 2.3 필터
- Liquid 오브젝트의 출력을 변화시킴
- **|**
    - 예) **\{\{ "hi" | capitalize \}\}**는 **hi**를 출력합니다.

## 3. 머리말
Liquid 태그를 사용하려면 반드시 
파일의 맨 처음에 세 개의 대시문자로 감싼 YAML 코드 조각  
해당 페이지에 대한 변수를 설정하는데 사용
- \-\-\-
    - 예) \-\-\-
        title: HOME
          \-\-\-

경로 설정하기  
지킬에서 pathsms _config.yml에서 정의된 url과 baseurl 변수가 사용된다. (참조: https://blog.jaeyoon.io/2017/12/jekyll-image.html)  
* url: damain + root path
* baseurl: subpath 👉 사이트가 도메인의 root가 아닌 subpath에 호스팅 된 경우 용이

#### 이미지 첨부하기
**1. HTML** 
* Absolute URL 
    * < img data-action="변수" src='\{\{ "파일경로" | relative_url \}\}' alt="이미지에 대한 설명" >
* Relative URL
    * < img data-action="변수" src='\{\{ "파일경로" | relative_url \}\}' alt="이미지에 대한 설명" >
위의 두 개가 똑같은데?  

**2. MarkDown**
* ! \[ Image Alt 텍스트 \]\(\{\{ site.url \}\}폴더경로\)
* ! \[ Image Alt 텍스트 \]\( http:// 폴더경로 \)
* ! \[ Image Alt 텍스트 \]\(\{\{ 폴더경로 | relative_url \}\}\)


참고 사이트
1. https://jekyllrb-ko.github.io/docs/structure/