---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_codingTest-3
# 제목 설정 (사용 언어로 작성)
title: 코딩테스트 - 입문자를 위한 정리
# 카테고리 설정 (1개)
category: 코딩테스트
# 태그 설정 ([태그1, 태그2, ...])
tags: [코딩테스트] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
#img: "" 
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
#published: false

##########################################################################################
# 👇 본격적으로 글을 작성하면 됩니다. 

---
<!-- outline-start -->
\[코딩테스트\] - 도저히 버틸 수가 없어서 정리했습니다.. 🌡️

<!-- outline-end -->
파이썬 알고리즘 인터뷰<br>

95가지 알고리즘 문제 풀이로 완성하는 코딩 테스트 
# 1부 코딩 인터뷰
## 1장 코딩 인터뷰
### 1.1 코딩 인터뷰를 위한 온라인 테스트 플랫폼
### 1.2 국내 기업의 코딩 테스트 플랫폼 활용 현황
### 1.3 온라인 코딩. 테스트의사전 준비사항
### 1.4 화이트보드 코딩 인터뷰 

<br>
<br>
<hr>

## 2장 프로그래밍 언어 선택
### 2.1 경진대화 통계로 알아본 언어 선호도
### 2.2 프로그래밍
* 루프
* 제네릭 프로그래밍
* 구조체
* 클래스

### 2.3 코딩 테스트에
<br>
<br>
<hr>

# 2부 파이썬
## 3장 파이썬
### 3.1. 파이썬에 대한 이해
이 책에서는 공식 인터프리터 CPython을 기준으로 합니다. (python= 3.7)

### 3.2 파이썬 문법
코딩 테스트에서 내 코드 생산성을 높여보자!
* 인덴트(indent)
    * 공식 가이드 PEP 8에 따라 공백 4칸이 원칙
    * 강제는 아니지만, 따르는 게 좋음
    * pycharm과 같은 개발도구를 활용하면 자동으로 준수함 

~~~python
# 1. 첫 번째 줄에 파라미터가 있다면, 파라미터가 시작되는 부분에 보기 좋게 맞춰주세요.
A = long_funtion_name(var_one, var_two,
                    var_three, var_four)

# 2. 첫 번째 줄에 파라미터가 없다면, 공백 4칸 인덴트를 한 번 더 추가하여 작성해 주세요.
B = long_function_name(
        var_one, var_two, var_three,
        var_fout):
print(var_one)
~~~
<br> 

* 네이밍 컨벤션(Naming Convention)
    * 파이썬의 변수, 함수명은 Snake Case를 따른다.
    * 각 단어를 밑줄(_)로 구분 *<span style="color:#BFBFBF">- pythonic way~</span>*
    * 출제자가 지키지 않았어도 제출자는 지켜주기
    * 면접관이 질문을 한다면? **“저는 PEP 8 및 철학에 따라 snake case 코딩을 지향합니다~”**
    * IDE를 사용한다면, 알아서 알려줄 것임 “경고 경고! snake case로 pythonic way를 티내세요” 

> 더 알아보기<br>
> snake case: ‘뱀 처럼 생긴 _’로 단어를 구분 (Python) <span style="color:#FF5277">twinkle_little_star</span><br>
> camel case: ‘낙~타’ 대소문자로 단어를 구분 (Java) <span style="color:#FF5277">twinkleLittleStar</span><br>
> pascal case: 첫 시작 문자**도** 대문자로 표현 <span style="color:#FF5277">TwinkleLittleStar</span>

<br>

* 타입 힌트
    * 파이썬은 대표적인 동적 타이핑 언어지만, 타입을 지정하여 명시적으로 선언할 수 있음
    * 가독성이 좋아지고 버그 발생 확률이 낮아진다.
    * 온라인 코딩 테스트에서 **$ pip install mypy**를 이용하면 타입 힌트 오류를 확인해 줌
        * **$ mypy 파일이름.py**
        * 파일이름.py: 잘못된 코드: error: Incompatible return value type (got “타입”, expected “타입”)

~~~python
# 변수에 타입 힌트를 명시했어요. —> a는 문자형, b는 정수형
a: str = “1”
b: int = 1

# 함수에 타입 힌트를 명시했어요. —> fn() 함수의 파라미터 c는 정수형, return은 bool형(True, False)
def fn(c: int) -> bool:
@@@
~~~

<span style=“color:#F20519”>주의!!</span>

~~~python
a: str = 1
type(a) # <class ‘int’> 출력
~~~

문자열로 선언하고 정수형을 할당하면, 정수형으로 변환되니 조심하세요! (동적 타이핑 언어 특징임~)
<br>
<br> 

* 리스트 컴프리헨션(List Comprehension)
    * 기존 리스트를 기반으로 새로운 리스트를 만들어 냅니다. (from python=2.0)
    * 단, 표현식이 2개 이하일 때 사용하세요.
    * map, filter 등의 함수형 기능과 Lamda Expresson 보다 가독성이 높음 
    
~~~python
list(map(lamda x: x + 10, [1,2,3])) # [11,12,13] 출력

############ 1부터 10사이의 홀수는 2를 곱하여 출력하기 ############
# 1-1 리스트 컴프리헨션을 사용
[n * 2 for n in range(1, 10+ 1) if n % 2 == 1] # [2, 6, 10, 14, 18] 출력 

# 1-2 리스트 컴프리헨션을 사용하지 않음 (반복문을 통해 리스트 생성)
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)
    print(a) # [2, 6, 10, 14, 18] 출력
######## 불필요한 리스트(a)를 만들어야 하고 코드도 길어졌어요 ########

####################### 딕셔너리 생성 #######################
# 2-1 리스트 컴프리헨션을 사용
a = {key: value for key, value in original.items()}

# 2-2 리스트 컴프리헨션을 사용하지 않음
a = {}
for key, value in original.items():
    a[key] = value
~~~
<br> 

* 제너레이터(Generator)
    * 2001년 (from python=2.2)
    * 루프의 Iteration 동작을 제어할 수 있는 루틴 형태입니다.
    * 기존 함수와 다른 점은?
        * 기존 함수: return 구문에서 값을 반환하고 종료
        * 제너레이터: yield 구문에서 중간값을 반환하고 함수는 계속 실행
        * **여기까지 실행 중이던 값을 내보낸다 = 양보한다**
    * 기존 함수에 비해 좋은 점은? 메모리가 엄청나게 절약됩니다!

> 예를 들어 임의의 조건으로 숫자 1억 개를 만들고 계산을 해야 한다면?<br>
> 숫자 1억 개를 어디에 보관해야하죠….? 내 메모리…🥲<br>
> 제너레이터는 메모리 부담 없이 필요할 때마다 숫자를 만들어 줍니다!<br> 

~~~python
################## 하나의 타입으로 제너레이터 생성 ####################
# 1. 제터레이터 생성 (생성은 하였으나, 종료 조건이 없어서 무한 반복)
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

# 2. 제너레이션 출력
get_natural_number() # <generator object get_natural_number at 0x10d3139d0>

# 3. 제너레이션에 종료 조건 부여 (1부터 100까지 출력)
g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

################# 여러 개의 타입으로 제너레이터 생성 ##################
def generator():
    yield 1
    yield "string"
    yield True

g = generator()
print(g) # <generator object generator at 0x10a47c678>
print(next(g)) # 1
print(next(g)) # ‘string’
print(next(g)) # True
~~~
<br> 

* range
    * 제너레이터의 방식을 활용하는 함수
    
~~~python
A = list(range(5))
print(A) # [0, 1, 2, 3, 4] 출력

B = range(5)
print(B) # range(0, 5)
print(type(range(5))) # <class ‘range’>

# for 문을 사용할 경우, 제너레이터의 next()를 호출한 것과 비슷함
for i in rage(5):
    print(i, end=‘ ‘) # 0 1 2 3 4 출력
~~~

~~~python
# A와 B의 길이는 같으나 메모리는 A >>> B 임
A = [n for n in range(10000)] # range에 값을 생성
B = range(10000) # range만 생성
~~~
<br>

* enumerate
    * ‘열거하다’
    * 순서가 있는 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴합니다.

~~~python
# 1. enumerate() 사용해보기
A = [1,2,3,4,5,6]
print(A) # [1, 2, 3, 4, 5, 6] —> 리스트를 그대로 출력

B = list(enumerate(A))
print(B) # [(0, 1), (1, 2), (2, 3), (4, 5), (5, 6)] —> 리스트에 인덱스를 포함하여 출력

# 2. enumerate()가 얼마나 효과적인지 살펴보기
A = ["a1", "a2", "a3"]

# 2.1 불필요한 a[i]를 사용해야 함
for i in range(len(A)):
    print(i, A[i])

# 2.2 굳~이 변수 하나를 따로 관리해야 함
i = 0
for v in A:
    print(i, v)
    i += 1

# 2.3 깔끔함!
for i, v in enumerate(A):
    print(i, v)
~~~
<br>

* // 나눗셈 연산자
    * /: 사칙연산 나누기 (float 형)
    * //: 몫 (int 형)
    * %: 나머지 (int 형)
    * divmod(나누어질수, 나눌수): 몫과 나머지 출력
<br>
<br>

* print
    * 코딩 테스트에서 요긴함
    * 실무에서는 debugging 혹은 TDD 방식을 사용
    * <span style=“color:#F20519”>자동으로 줄바꿈을 해줌</span>

~~~python
# 1. 출력할 값을 (,)로 구분해주면, 한 칸 공백으로 출력됨
print("A1", "B2") # A1, B2 출력 

# 2. sep 파라미터를 이용하여 구분자를 (,)로 지정할 수 있음
print("A1", "B2", sep=",") # A1, B2 출력

# 3. end 파라미터를 이용하여 줄바꿈을 하지 않도록 제한 —> end를 공백 처리
print("A1", end=" ")
print("B2") # A1 B2 출력

# 4. join()으로 묶어서 리스트를 출력
A = ["A", "B"]
print(" ".join(A)) # A B 출력 

# 5. 연산하여 출력
A = 1
B = "apple"

# 5.1 .format을 이용
print("{0}: {1}".format(A + 1, B)) # 2: apple 출력
print("{}: {}".format(A + 1, B)) # 2: apple 출력

# 5.2 f-string 이용
print(f"{A + 1}: {B}") # 2: apple 출력 — python=3.6 이상만 지원 —> 얘를 기억할 것!
~~~
<br> 

* pass
    * 코드의 전체 골격을 잡아 놓을 때 사용 (=mockup 인터페이스 구현)
    * 클래스야 아직 다 만든 게 아니니깐 실행은 하지말아줘!

~~~python
class MyClass(objcet):
    def method_a(self):
        pass
    def method_b(self):
        print(“Method B”)

c = MyClass()
~~~
<br> 

* locals()
    * 로컬 심볼 테이블 딕셔너리를 가져오는 메소드
    * 로컬에 선언된 모든 변수를 조회할 수 있음
    * 기존 변수의 값을 변경할 수는 없지만, 새로운 변수를 생성하거나 값을 변경할 수는 있음
        * **import pprint**와 **pprint.pprit(locals())**를 이용하면 보기 좋은 코드 떡을 만들어 줌
    * 장점이 뭘까? 디버깅에 요긴함
<br>
<br>
<br>

### 3.3 코딩 스타일
채용을 위한 코딩 테스트에서, 코드의 품질은 중요하다. “왜 코드를 이렇게 작성했어요?” 등의 정성적인 질문에 답할 수 있어야 한다.

> 비법
> Pycharm과 같은 IDE를 사용하면, PEP 8 기준으로 자동으로 경고를 띄어주니깐 참고
> 1. 변수명은 snake_case, 주석은 영어로 작성할 것
> 2. 리스트 컴프리헨션은 역할별로 줄 바꿈을 해주고 표현식은 2개 이하로 할 것
> 3. 구글 파이썬 스타일 가이드를 참고할 것
> 4. import this를 참고할 것

<br>
<br>
<hr>

## 4장 빅오, 자료형

### 4.1 빅오
**big-O**는 아~주 중요하니깐 꼭! 이해해야 합니다. 간단히 요약하면, 입력값이 커질 때 알고리즘 실행 시간과 메모리 사용 크기가 어떻게 증가하는지 알려줍니다.
* 시간 복잡도(Time Complexity)
* 공간 복잡도(Space Complexity)

* 상한과 최악
* 분할 상환 분석
* 병렬화

### 4.2 자료형
* 파이썬 자료형
* 원시 타입
* 객체

<br>
<br>
<hr>

## 5장 리스트, 딕셔너리
### 5.1 리스트
* 리스트 활용 방법
* 리스트 특징

### 5.2 딕셔너리
* 딕셔너리의 활용 방법
* 딕셔너리 모듈

<br>
<br>
<hr>

## 6장 문자열 조작

<br>
<br>
<hr>

# 3부 선형 자료구조
## 7장 배열
<br>
<br>
<hr>

## 8장 연결 리스트
<br>
<br>
<hr>

## 9장 스택, 큐
<br>
<br>
<hr>

## 10장 데크, 우선순위 큐
<br>
<br>
<hr>

## 11장 해시 테이클
<br>
<br>
<hr>


# 4부 비선형 자료구조
## 12장 그래프
<br>
<br>
<hr>

## 13장 최단 경로 문제 
<br>
<br>
<hr>

## 14장 트리
<br>
<br>
<hr>

## 15장 힙
<br>
<br>
<hr>

## 16장 트라이
<br>
<br>
<hr>


# 5부 알고리즘
## 17장 정렬
<br>
<br>
<hr>

## 18장 이진 검색
<br>
<br>
<hr>

## 19장 비트 조작
<br>
<br>
<hr>

## 20장 슬라이딩 윈도우
<br>
<br>
<hr>

## 21장 그리디 알고리즘
<br>
<br>
<hr>

## 22장 분할 정복
<br>
<br>
<hr>

## 23장 다이나믹 프로그래밍
