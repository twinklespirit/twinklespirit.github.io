---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_datastructure_2
# 제목 설정 (사용 언어로 작성)
title: (자료구조) 선형 자료구조
# 카테고리 설정 (1개)
category: 개인공부
# 태그 설정 ([태그1, 태그2, ...])
tags: [자료구조, 알고리즘] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/179442964-74ed7772-8a3b-4b1c-bee9-989a62bcda14.png" 
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-19 12:00:00 +0900

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

\[자료구조\] - 순차적 자료구조(배열, 스택, 큐, 데큐, 연결리스트)

<!-- outline-end -->
참고한 스승님 [클릭](https://www.youtube.com/watch?v=PIidtIBCjEg&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK)

<br>

# 순차적 자료구조

* 자료가 순차적(Sequential), 연속적으로 저장된 자료구조 <span style="color:red">너무 중요함!!</span>

<br>

## Introduction

### [배열과 리스트](#5-배열과-리스트)<br>

![img_74](https://user-images.githubusercontent.com/105165938/179845596-6aa4eefb-989b-4daa-b4f6-b3d51c07a149.jpeg)<br>

* Index로 임의의 원소를 접근
    * [] 연산자 
        * ex) A\[2\] -> -1을 추출 
        * RAM(emory)(주소)만 있으면 $O(1)$ 가능!!
        1. 주소가 가리키는 객체에 접근 (1번)
        2. data를 추출 (1번)
    * 맨 마지막에 요소를 삽입, 삭제하는 연산자 append(), pop() 
        1. 주소가 가리s키는 객체에 접근 (1번)
        2. data를 삽입 혹은 삭제 (1번)
        * $O(1)$ 
    * 임의의 위치에 요소를 삽입, 삭제하는 연산자 insert(index, val), remove(val)
        * 중간에 위치한 요소에 삽입 혹은 삭제 시 
            1. 빈자리 발생!!!
            2. 빈자리 메꾸기 위해 요소들 자리 이동!!
        * 어느 위치에 있는 요소인지에 따라 결과가 상이할 것임. 최악의 경우 $O(n)$

<br>



### Stack, queue, dequeue
* 제한된 접근(삽입, 삭제)만 허용

<br>

1. (Stack) LastInFirstOut(LIFO)
    * '입으로 먹고 입으로 똥싸는 말미잘'<br>

    ![img_71](https://user-images.githubusercontent.com/105165938/179842058-21a20cd7-3448-47d1-91cc-ca379d8c3c74.jpeg)<br>

    <br>

2. (Queue) FirstInFirstOut(FIFO)
    * '입으로 먹고 똥꼬로 똥싸는 사람'<br>

    ![img_72](https://user-images.githubusercontent.com/105165938/179842809-d28145e4-bb89-4fe9-b1cc-8ec3cd634f57.jpeg)<br>

    <br>

3. (Dequeue) Stack + Queue<br>

    ![img_73](https://user-images.githubusercontent.com/105165938/179843058-a71dde7a-eb6d-4c77-bdb1-7454778ede9a.jpeg)

<br>



### Linked List
 
* != Python List (또는 배열)
* 어떤 값(데이터, 다음 노드 위치)들이 **순차적으로 연결되어 있는** 리스트 
    * 배열은 어떤 값을 <u>연속된 메모리에 순차적으로</u> 저장<br>

![img_70](https://user-images.githubusercontent.com/105165938/179841555-41ca86de-1bfd-443b-acba-89c22ee9844a.jpeg)<br>
* 딱~봐도 Index로 접근 불가


<br><br>
<hr>

## 5. 배열과 리스트

### 배열 (C언어)<br>

* index로 값에 접근
![img_75](https://user-images.githubusercontent.com/105165938/179848119-22a9c3d4-3510-41df-be65-86d9c6a28c62.jpeg)<br>
* 읽기, 쓰기 연산자를 제공한다.

~~~c
#include <stdio.h>

int main()
{
    // 배열 선언
    int A[3] = {2,4,0,5};

    // 배열의 주소값 선언
    //int *p = &A[0];

    // 읽기, 쓰기 연산
    A[2] = A[2] + 1;
    printf("%d ", A[2]); // 1출력
    
    // index의 범위를 초과한다면?
    printf("%d ", A[4]); // warning: array index 4 is past the end of the array
}
~~~

<br>

### 리스트 (Python)
* <span style="color:red">많이 쓸 거니깐 장점과 단점을 잘 알아두자!</span>
* Index로 값에 접근함
![img_76](https://user-images.githubusercontent.com/105165938/179848529-5f3193a1-c9e3-4b6d-98a8-e35cbe9d5adc.jpeg)<br>

<br>

* 배열보다 더 강력하고 유연함
    1. (배열보다 훨~씬 많은 유형에 대한) 다양한 연산자 제공<br>
    ![img_77](https://user-images.githubusercontent.com/105165938/179849112-7caed034-8aa3-4f43-9112-a6dcf58023ad.jpeg)<br>
    2. 용량을 내부적 요인 덕분에 자동으로 조절 (<span style="color:red">dynamic array</span>)<br>

    ~~~python
    import sys

    A=[] # 빈 리스트 선언
    print(sys.getsizeof(A)) # A가 차지하는 바이트 수 리턴: 56출력

    A.append(10)
    print(sys.getsizeof(A)) # 88출력
    ~~~

    * 교수님이 말씀하신 시간보다 더 걸렸다. (M1 왜그래😂)<br>
    * 어떻게 용량이 자동으로 조절될 수 있는지 그림으로 이해하자
    ![img_78](https://user-images.githubusercontent.com/105165938/179849525-df8bf43d-1bb2-4dab-93a1-cf69f7fb3e38.jpeg)<br>[추가정보](https://docs.python.org/ko/3.8/c-api/memory.html)<br>

    * 조금 더 자세히 설명한 그림을 봐보자<br>
    ![img_79](https://user-images.githubusercontent.com/105165938/179850888-44bfd847-bb3b-488e-88a5-b4696b6de703.jpeg)<br>

<br>

> 정리하자!
> * 배열은 index로 특정한 위치에 있는 어떤 값을 읽거나 쓰는데 상수시간 $O(1)$ 이 걸린다.
> * 리스트는 index로 특정한 위치에 있는 어떤 객체를 다양한 연산자로 연산할 수 있으며, 용량을 자동으로 조절할 수 있다. 

<br><br>
<hr>

## 6. 스택

