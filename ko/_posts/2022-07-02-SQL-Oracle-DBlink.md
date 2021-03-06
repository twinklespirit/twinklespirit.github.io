---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_SQL_Oracle_DBlink
# 제목 설정 (사용 언어로 작성)
title: DB link 사용하기
# 카테고리 설정 (1개)
category: Oracle 
# 태그 설정 ([태그1, 태그2, ...])
tags: [sql] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "" 
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-02 19:00:00 +0900

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

<!-- outline-end -->
## Ch01 연계 데이터 구성
서로 다른 두 시스템, 장치, 소프트웨어가 정보를 교환할 수 있도록 이어주는 중계 역할을 합니다.

### 1. 연계 요구사항 분석
* 분석 기법
    * 사용자 인터뷰
    * 체크리스트: 시스템 운영 환경, 성능, 보안, 데이터 발생 주기
    * 설문지: 연계 필요 데이터, 연계 주기
    * 델파이: 각 분야 전문가의 경험을 신뢰
    * 브레인스토밍: 소속 인원의 자발적인 아이디어
<br>

* 분석 참고 문서
    * 공통 코드 정의서: 코드 ID, 코드명, 코드 설명 등
    * 테이블 정의서: 
    * 응용 프로그램 구성도
    * 시스템 구성도
<br>

* 분석 절차
    1. 시스템 현황 확인
    2. 정의서 확인
    3. 체크리스트 작성
    4. 인터뷰 및 면담
    5. 연계 요구사항 분석서 작성
<br>

### 2. 연계 시스템 구성
* 구성
    * 송신 시스템
    * 수신 시스템
    * 중계 서버: (생략 가능)
    * 

### 3. 연계 데이터 식별 및 표준화 -하~나도 안 중요하니깐 나중에 실무 때 참고만 하기
* 연계 데이터 식별
    * 대내외 시스템 연계를 위해 참고 
    * 대외 혹은 내외 표기 (대외 기관일 경우, 기관명도 함께 표기)
    * 시스템 ID
    * 시스템 한글명, 영문명
    * 시스템 설명
    * 시스템 위치
    * 네트워크 특성
    * 전용 회선 정보
    * IP/URL
    * Port
    * Login
    * DB 정보
    * 담당자 정보
<br>
<hr>

## Ch02 연계 메커니즘 구성
연계 방법과 주기를 설계하기 위한 메커니즘

### 1. 기본 개념
* 필수 구성 요소
    * 송신 시스템: 연계 데이터를 생성하여 송신
    * 수신 시스템: 연계 데이터를 수신하여 변환 처리 후 DB에 반영
 <br>

1. 직접 연계 방식
    * 장점: 단순 연결, 적은 비용, 좋은 성능
    * 단점: 높은 결합도, 암복호화 처리 못함, 제한적
2.  간접 연계 방식 
    * 장점
    * 단점 

 <br>

* 연계 기술
    * 직접 연계
        * DB link
        * DB connection
        * API/Open API
        * JDBC
        * Hyper Link
    * 간접 연계
        * EAI
        * ESB
        * Socket

### 2. 연계 장애 및 오류 처리 구현

## Ch03 내외부 연계 모듈 구현


### 1. 구현 환경 구성 및 개발
1. EAI
    * Enterprise Application Integration
    * 기업 내 서로 다른 플랫폼 및 애플리케이션을 연계
        * ERP(Enterprise Resource Planning)
        * CRM(Customer Relationship Management)
        * SCP(Supply Chain Planning)
    * 정보를 전달, 연계, 통합이 가능하게 해주는 솔루션
    * 구성요소
        * EAI platform
        * Adapter
        * Broker
        * Message queue
        * Business Workflow
    * 구축 유형
        * Point-to-point
        * Hub & Spoke
        * Meesage Bus
        * Hybrid
<br>

2. ESB
    * d
    * d
<br>

3. Web Service
    * 네트워크에 분산된 정보를 서비스 형태로 개방하여 표준화된 방식으로 공유
    * 서비스 지향 아키텍쳐
    1. SOAP(Simple Object Access Protocol)
    2. UDDI(Universal Description, )
    3. WSDL

### 2. 연계 테스트 및 검증