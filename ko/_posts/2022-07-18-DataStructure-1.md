---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_datastructure_1
# 제목 설정 (사용 언어로 작성)
title: 자료구조 - 1 자료구조와 알고리즘 기본
# 카테고리 설정 (1개)
category: 개인공부
# 태그 설정 ([태그1, 태그2, ...])
tags: [자료구조, 알고리즘] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/179442964-74ed7772-8a3b-4b1c-bee9-989a62bcda14.png" 
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-18 12:00:00 +0900

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
\[자료구조\] - 자료구조와 알고리즘, 알고리즘 시간복잡도, Big-O 표기법

<!-- outline-end -->
참고한 스승님 [클릭](https://www.youtube.com/watch?v=PIidtIBCjEg&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK)

#### 강의 듣는 팁
1. python은 각자 공부하기
2. 자료구조 코딩 과제를 해결하며 훈련하기

## 1. Introduce

![img_53](https://user-images.githubusercontent.com/105165938/179443354-8ff81a5d-1b09-4d21-ad00-5c16ce5284c3.png)<br>
1. Big-O
2. Array(List), Stack Queue, Dequeue
3. Linked List
4. Hash table: 현실에서 가장 많이 쓰임
4. Tree: 복잡하고 어려움
    * Priority Queue
    * 이진트리
    * 이진탐색트리
    * 균형이진탐색트리
5. Graph: 시간이 부족할 예정 (추후 개인적으로 학습하자!)

<br><br>
<hr>

## 2. 자료구조와 알고리즘

### 자료구조
* 자료를 담는 구조

<br>

* 구성
    * 자료(data) (컴퓨터에 담을 수 있는 저장공간(memory)이 필요)
    * 연산자 (data를 read, write, insert, delete, search 해주는 친구들) 👉 자료구조를 구분하는 기준

    <br>

* [자료구조의 예](#자료구조의-예)

<br>

### 알고리즘
* 입력 data로 유한한 연산들을 사용하여 원하는 정답을 출력
* [등장 배경(인류 최초의 알고리즘)](#인류-최초의-알고리즘)

<br>

#### 자료구조의 예

1. 변수<br>
![img_54](https://user-images.githubusercontent.com/105165938/179448459-f5bf6450-f2aa-4468-a8e3-714710c8d35d.jpeg)<br>
* 파이썬의 변수는 값을 저장하는 것이 아니라, **값의 주솟값을 저장**하는 것임을 기억! (= 값을 참조한다)
* 이유: 각각의 값은 객체(object)로 저장되어 있음

<br>

2. 배열(array)과 리스트(list)<br>
![img_55](https://user-images.githubusercontent.com/105165938/179448767-88cd9585-05b2-44e6-95c7-303ba4359ef5.jpeg)<br>

<br>

#### 인류 최초의 알고리즘
* 최대공약수 == GCD(Greatest Common Divisor) 계산 알고리즘
    * 두 자연수 중 최대 공약수를 가장 큰 수(최대공약수)
* 👆 믿거나 말거나 GCD를 만든 사람 이름이 알고리즘이라고 함

<br>

* GCD(8,12)이란? 공약수 {1,2,4} 중의 최대값인 4를 구함
    1. 빼기(-) 연산 이용<br>
    ![img_56](https://user-images.githubusercontent.com/105165938/179450518-1404b590-8033-4dbe-8b22-69507ebf6a85.jpeg)<br>

    ~~~python
    def gcd(a,b):
        while a != 0 and b != 0: # 둘 중 하나가 0이 될 때까지
            if a > b: a = a-b
            else: b = b-a
        return a+b # 둘 중 하나는 0이니깐!
    ~~~
    * 만약에 gcd(2,100)라면? 50번을 반복.. -> gcd(2,0)
    * "처음부터 나머지를 구해보자!"

    <br>

    2. 나머지(%) 연산 이용

    ~~~python
    def gcd(a,b):
        while a != 0 and b != 0:
            if a > b: a = a%b
            else: b = b%a
        return a+b
    ~~~

    <br>

    3. 재귀(recursion) 이용

    ~~~python

    ~~~

    <br>

> 정리하자!
> * GCD를 구하는 방법
> 1. gcd_sub
> 2. gcd_mod
> 3. gcd_rec

<br><br>
<hr>

## 3. 알고리즘 시간복잡도
* 우리가 사용하는 자료구조와 자료구조를 활용하여 어떤 문제를 해결하는 알고리즘의 성능을 측정하고 비교하는 방법을 알아보자

<br>

### 알고리즘 실행 프로세스<br>

![img_57](https://user-images.githubusercontent.com/105165938/179467245-06941291-7a97-422f-8356-383741e11d9e.jpeg)<br>
1. 자료구조와 알고리즘을 프로그래밍 언어를 이용하여 코드로 작성한다.
2. 컴퓨터에서 코드가 실행된다.<br>
👉 우리는 컴퓨터에서 코드가 실행되는 시간을 측정한다.<br>

<br>

### 알고리즘 성능에 영향을 주는 요인

1. HW/SW 환경
    * 내 컴퓨터 != 친구 컴퓨터
        * CPU(register, cash), Memory(ram) 성능이 다르다.
    * 컴퓨터의 성능은 algorithm 수행시간에 영향을 미친다.
    * 따라서 동일한 algorithm이라도 두 컴퓨터에서의 알고리즘 수행 시간(= 알고리즘 성능)은 다를 것이다. 

    <br>
    
2. 입력되는 데이터의 개수(= input data의 크기)
    * N(100개의 data) != M(100,000개의 data)
    * 일반적으론 처리해야 할 data가 많을수록 algorithm 수행시간이 길어진다.
    * N과 M의 algorithm 수행 시간(= 성능)은 다르다.

<br>

### 알고리즘 성능에 영향을 주는 요인을 차단하는 방법

#### (1) 가상 컴퓨터 + 가상 언어 + 가상 코드를 사용
* HW/SW로부터 독립적인 상태
*  <u>성능에 영향을 주는 요인 1.</u>를 해결

<br>

1. virtual machine(컴퓨터)
    * 발달 과정
        * Turing Machine -> von Neumonn: RAM(Random Acess Machine)
        * RAMachine(컴퓨터) != RAMemory(메모리) (개념적으론 같음)

    <br>

    * RAM
        * 우리가 만든 알고리즘이 수행될 컴퓨터(알고리즘 성능 측정)
        * CPU + Memory로 구성
            * Memory: program, program이 다루는 data
            * CPU: <span style="background-color:#fffca7; color:black"> 연산장치</span>, 제어장치, 레지스터
                1. Memory와 접촉
                2. Memory에 있는 data를 가져와서 읽기, 쓰기 등의 기본연산을 반복 수행
                3. 결과를 다시 Memory로 반환

                <br>

    > 우리에게 중요한 **기본연산**!
    > * 1단위 시간 내에 수행되는 연산의 모음
    >   * 배정, 대입, 복사 연산
    >       * A = B
    >           1. data B를 읽어온다. (연산횟수: 1번)
    >           2. data A에 값을 쓴다. (연산횟수: 1번)
    >   * 산술연산 +, -, *, /
    >       * 주의! (%, 반올림, 올림, 버림): RAM에서는 단위연산(X), 강의에서는 단위연산으로 간주(O)
    >   * 비교연산 >, >=, <, <=, ==, !=
    >       * A < B
    >           1. A - B 산술연산을 수행한다. (연산횟수: 1번)
    >           2. (A-B)가 0보다 작은지 비교연산을 수행한다. (연산횟수: 1번)
    >   * 논리연산: and, or, not
    >   * 비트연산: bit-and, bit-or, bit-not

    <br>

2. Virtual language
    * 아래의 연산들을 표현할 수 있는 언어
    * 기본연산
    * 비교연산: if, if else, if else if else
    * 반복연산: for, while
    * 함수: 정의, 호출, return
    
    <br>

3. Virtual Code == Pesudo code
    * 단위시간에 수행되는 기본연산을 모아놓은 것 (기본연산을 반복)
    * 가상의 언어로 작성한 코드
    * 실제 작동하는 것이 아니라 시뮬레이션을 한다고 생각하면 됨
    
    <br>

    > 아래의 알고리즘은 단위 연산이 몇 번 수행이 될까? <br>
    > ![img_58](https://user-images.githubusercontent.com/105165938/179497966-14884fe8-b466-4ce7-9243-8e1afa24a043.jpeg)<br>
    > * 기본 연산을 총 7번 수행하므로 7단위 시간이 필요하다.
    > * 참고: 단위 연산 수행 횟수가 많을수록 알고리즘 수행 시간을 길어진다.
    > * "만약! 입력 크기에 대한 경우의 수가 무한히 많으며, 그에 따른 입력값의 경우의 수도 무한히 많다면, 알고리즘의 성능은 어떻게 측정할까?" 

    <br>

#### (2) 입력되는 데이터 개수의 경우를 예측
1. 가장 좋은 방법: 입력 가능한 모든 경우에 대한 기본연산 횟수를 구하고 평균을 낸다. (👉 현실적으로 불가)
2. 차선 방법: 가장 안 좋은 입력(worstcase input)에 대한 기본연산 횟수를 측정한다.
    * worstcase time complexity
    * 어떤 입력에 대해서도 worstcase time case보다 수행 시간이 크지 않다.<br>
        ![img_59](https://user-images.githubusercontent.com/105165938/179504431-db175f0e-1498-4924-845e-d09d0a024147.png)<br><br>
    ![img_60](https://user-images.githubusercontent.com/105165938/179504326-1243f5e4-3fbf-4ed4-ab24-17e84e3af4e8.jpeg)<br>
    $T(n)=2n-1$ 이다. $n=6$ 이라면, $T(6)=12-1=11$ 이다.<br>

<br>

> 🗣️ 알고리즘 수행시간은 입력이 최악인 경우에 사용되는 기본 연산 횟수로 정의한다.

예를 들어 익혀보자!<br>![img_61](https://user-images.githubusercontent.com/105165938/179598654-528d627c-185f-4d90-9b5a-6e673374d5b4.jpeg)<br>
* algorithm sum1과 sum2를 비교해보면,
* $n$ 이(input data의 개수) 커질 수록, sum1은 $n$만큼, sum2는 $n^2$만큼 비례하여 연산 횟수가 증가한다. (= 수행시간이 길어진다.)
 
<br><br>
<hr>

## 4. 알고리즘 시간 복잡도 Big-O 표기법

* 알고리즘 수행시간 == 최악의 경우의 입력에 대한 기본 연산 횟수
* 가장 좋은 방법은 아니지만, [가장 좋은 방법](#2-입력되는-데이터-개수의-경우를-예측)은 현실적으로 불가능하기 때문에 차선책을 적용함<br>

<br>

* 위에서 살펴본 algorithm 3개의 시간복잡도를 비교해 보자
![img_62](https://user-images.githubusercontent.com/105165938/179611392-efbef1f9-2c9a-4b60-bddd-c8e158d1d836.jpeg)<br>
* 전체적으로 n이 커질 수록 실행 시간은 algorithm 1 < algorithm 2 < algorithm 3으로 걸린다.
    * algorithm 1: 선형적으로 증가 (1->3->5->7)
    * algorithm 2: 선형적으로 증가 (5->9->13->17)
    * algorithm 3: 비선형적으로 증가 (4->10->19->31)

1. algorithm 2는 algorithm 1 수행 시간의 2배가 걸린다.
2. algorithm 3은<br>
    $n < 3\over 5$ 이면 algorithm 2보다 빠르고<br>
    $n > 3\over 5$ 이면 algorithm 2보다 항상 느리다.<br>
3. algorithm 3은 algorithm 1보다 항상 느리다.

<br>

> 🗣️ 입력 데이터(N) 증가에 따른 algorithm 수행시간은 algorithm 최고차항과 비례하게 증가한다. **(최고차항 == 수행시간의 증가률)**

<br>

### Big-O 표기법

* 수행시간 $T(n)$ = 함수값을 결정하는 최고차항으로 간단하게 표기

<br>

* 빅오 표기 방법
    1. 최악의 경우의 입력에 대한 수행시간의 최고차항만 남긴다.
    2. 최고차항의 계수(상수)를 생략한다.
    3. Big-O(최고차항)을 넣어 완성한다.

<br>

> 집합으로 이해하자!<br>
> ![img_63](https://user-images.githubusercontent.com/105165938/179613351-00e22ef6-4d74-4094-af89-a3f67afabd37.jpeg)<br>
> * 그림과 같이 "원소구나!"라고 이해하면 됨!
> * Quiz. $T_1(n)=2n-1$ 과 $T_1(n)=4n-1$ 은 두 배 차이 나는데, 어떻게 같은 시간으로 간주하죠??
> * Answer. 증가률의 관점에서 상수 시간은 그닥 중요하지 않습니다.^__^

<br>

* 예를 들어보자!<br>
![img_64](https://user-images.githubusercontent.com/105165938/179619907-4da5af95-2a4a-4574-86f9-4aa2e094149f.jpeg)<br>

#### 숙제
1. 시그마에 대해 공부하기
2. 로그와 상수의 변환, 비교 공부하기

> 수학을 알아보자!
> - 추후 예정


