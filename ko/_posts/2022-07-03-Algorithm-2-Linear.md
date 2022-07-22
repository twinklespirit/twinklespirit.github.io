---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_algorithm_2
# 제목 설정 (사용 언어로 작성)
title: 코딩테스트 - 입문자를 위한 정리 2
# 카테고리 설정 (1개)
category: 개인공부
# 태그 설정 ([태그1, 태그2, ...])
tags: [코딩테스트] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/178579982-e69ba60f-82ce-4be5-8ac5-d6a57f8c9789.png" 
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-09 3:00:00 +0900

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

\[코딩테스트\] - 도저히 버틸 수가 없어서 정리했습니다.. 🌡️

<!-- outline-end -->

# 3부 선형 자료구조

## 7장 배열
<br>
<br>
<hr>






## 8장 연결 리스트

> 🗣️ 연결 리스트는 데이터 요소의 선형 집합으로, 데이터의 순서가 물리적인 순서대로 저장되지는 않는다.

* 참고 문헌
    1. [파이썬 알고리즘 인터뷰](https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+%EC%9D%B8%ED%84%B0%EB%B7%B0&oq=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+%EC%9D%B8%ED%84%B0%EB%B7%B0&aqs=chrome.0.0i355i512j46i512j0i512l8.5653j0j7&sourceid=chrome&ie=UTF-8)
    2. [생활코딩](https://www.youtube.com/watch?v=sq49IpxBl2k)
    3. []

<br>

![img_28](https://user-images.githubusercontent.com/105165938/178834084-2820d704-4a1e-4525-af92-4a6bfa829220.png)<br>
*© 이미지 출처: https://www.youtube.com/watch?v=LRfLzM5uVDg*<br>

<br>

* 선행 지식
    * 

<br>

* 최소한의 구성
    * HEAD -> HEAD' data field -> link field's datafiled
    * HEAD
    * Data field
    * Link field
    
* Computer sicence에서 배열과 함께 가장 기본이 되는 선형 자료구조
* 추상 자료형 ADT(Abstract Data Type) 구현의 기반
* 동적으로 새로운 노드를 삽입하거나 삭제하기가 간편하며, 연결 구조를 통해 물리 메모리를 연속적으로 사용하지 않아도 되기 때문에 관리하기 쉬움
* 데이터를 구조체로 묶어서 포인터로 연결한다는 개념은 여러 가지로 활용할 수 있다. 
* 실제 컴퓨터의 물리 메모리에는 구조체 각각이 서로 연결된 형태로 구성되어 있으며, 메모리 어딘가에 흩뿌러진 형상이다.
* 배열과는 달리 특정 인덱스에 접근하기 위해서 전체를 순서대로 읽어야 한다. 상수 시간에 접근할 수 없다.
* 탐색: O(n)
* 시작 또는 끝 지점에 아이템을 추가, 삭제, 추출하는 작업: O(1)

* 등장배경
* 1995 랜드연구소 앨런뉴얼과 친구들이 만든 IPL 언어의 기본 자료구조
* -> 인공지능, 체스 프로그램 개발된 언어



#### 문제 1. 팰린드롬 연결 리스트

Solution
팰린드롬이 무엇일까?
일반적인 스택 자료구조는 마지막 요소만 추출할 수 있지만
파이썬의 리스트는 pop()에 인덱스를 지정할 수 있어서, 얼마든지 원하는 위치를 추출할 수 있다.

1. 리스트를 이용

~~~python

# 리스트 만들기

def isPalindrome(self, s: str) -> bool:


~~~

#### 문제 2. 두 정렬 리스트의 조합

~~~python
~~~

#### 문제 3. 역순 연결 리스트 1

~~~python
~~~

#### 문제 4. 두 수의 덧셈

~~~python
~~~

#### 문제 5. 페어의 노드 스왑

~~~python
~~~

#### 문제 6. 홀짝 연결 리스트

~~~python
~~~

#### 문제 7. 역순 연결 리스트 2

~~~python
~~~

<br>
<br>
<hr>

## 9장 스택, 큐
너~무 고전적인 자료구조라, 거의 모든 애플리케이션에 사용되었다.
* 스택
    * LIFO(**Last**-In-**First**-Out)
    * '잔뜩 쌓아올린 접시를 꺼내보자!'
    * 리스트가 스택의 모든 연산을 지원
* 큐
    * FIFO(**First**-In-**First**-Out)
    * '놀이기구 타야하니깐 줄서보자!'
    * 리스트가 큐의 모든 연산을 지원 (**성능을 위해서는 데크를 추천**)
        * why? 리스트 동적 배열

### 1. 스택
* 주요 연산
    * push(): 요소를 컬렉션에 추가
    * pop(): 가장 마지막으로 삽입된 요소를 컬렉션에서 제거
<br>

* 기원
    * 1946 앨런 튜링
    * 서브루틴 호출하는 과정(bury), 되돌아오는 과정(unbury)
    * 컴퓨터 서브루틴에 대한 정보를 저장하는 자료구조로 사용 (=> Call Stack)
<br>

* 
* 연결리스트를 이용한 스택 ADT 구현 (ADT: Abstrack Data Type)

~~~python
# Define a class containing a linked list
class Node:
    # initialization function
    def __init__(self, item, next):
        self.item = item # node's value
        self.next = next # pointer to the next node

# Define a class that implements operations on the stack.
class Stack:
    def __init__(self):
        self.last = None

    # While adding an element to a linked list
    def push(self, item):
        # the last value is set to next
        self.last = Node(item, self.last)
    
    # 마지막 아이템을 끄집어내고
    def pop(self):
        item = self.last.item
        # last 포인터를 한 칸 앞으로 전진
        self.last = self.last.next
        return item
~~~

#### 문제 1. 유효한 괄호
* 문제: 괄호로 된 입력값이 올바른지 판별하라.
    * 입력: ()[]{}
    * 출력: true
<br>

* 풀이: 
    1. \(, \[, \{ 은 스택에 push
    2. \), \], \} 은 스택에 pop



#### 문제 2. 중복 문자 제거
#### 문제 3. 일일 온도

### 2. 큐
#### 문제 1. 큐를 이용한 스택 구현
#### 문제 2. 스택을 이용한 큐 구현
#### 문제 3. 원형 큐 디자인

<br>
<br>
<hr>

## 10장 데크, 우선순위 큐
### 1. 데크
#### 문제 1. 원형 데크 디자인
### 2. 우선순위 큐
#### 문제 2. K개 정렬 리스트 병합
<br>
<br>
<hr>

## 11장 해시 테이블
<br>
<br>
<hr>

