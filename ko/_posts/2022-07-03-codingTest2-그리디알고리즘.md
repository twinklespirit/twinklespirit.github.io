---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_condingTest_02
# 제목 설정 (사용 언어로 작성)
title: 코딩테스트 2 - Greedy algorithm
# 카테고리 설정 (1개)
category: 코딩테스트 
# 태그 설정 ([태그1, 태그2, ...])
tags: [코딩테스트] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: ":python-coding.jpg" 
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-01 21:00:00 +0900

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
[ 코딩테스트 ] 그리디 알고리즘

<!-- outline-end -->
# 그리디 알고리즘
* 현재 상황에서 지금 당장 좋은 것만 고르기!
* 정당성 분석: 단순히 좋아보이는 것을 반복적으로 선택해도 최적의 해를 보장할 수 있는지 검토하자!
* 일반적인 상황에서는 보장할 수 없어 유용하지 않지만, 코딩 테스트에서는 유용함 (Why? 출제자가 보장하게끔 문제를 만듦)

## 문제1. 거스름 돈 
~~~python
n = 1260
count = 0

# 거슬러 줄 수 있는 화폐 종류
arry = [500, 100, 50, 10]

# 큰 단위의 화폐부터 차례대로 확인
for coin in array:
    count += n // coin
    n %= coin

print(count)
~~~

시간복잡도는 O(K), 화폐의 종류만큼 걸린다.

~~~c++
#include <bits/stdc++.h>
using namespace std;

int n =1260;
int cnt;

int coinTypes[4] = {500, 100, 50, 10}

int main(void) {
    for (int i=0; i<4; i++){
        cnt += n / coinTypes[i]
        n %= coinTypes[i]
    }
    cout << cnt << '\n';
}
~~~

## 문제2. 1이 될 때까지
어떤 수 N과 K가 있다. N이 1이 될 때까지 아래의 두 과정 중 하나를 반복하여 수행해야 한다. **최소 횟수를 수행하는 프로그램**을 작성하라.<br>
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택<br>
1. N에서 1을 빼기
2. N을 K로 나누기

조건<br>
* 풀이시간: 15분
* 시간제한: 2초
* 메모리제한: 128MB
* 입력: N, K는 공백을 기준으로 자연수

1. 내가 푼 것
~~~python
# 입력
N, K = map(int, input().split(" ")) # map(함수, 자료): 자료에 함수를 적용
count = 0

# 처리
while N > 1:
    print(N, end=" ")
    if N%K == 0:
        count += 1
        N = N//K
    else: 
        count += 1
        N -= 1
print( )
print(count)
~~~

2. 강의에서 나온 것
~~~python
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
~~~

## 문제3. 곱하기 혹은 더하기
문자열 S는 각 자리에 숫자가 들어있다. 왼쪽부터 숫자 사이에 X 혹은 + 연산자를 넣어 가장 큰 수를 만들어라. <br>
단, 연산은 왼쪽부터 진행한다.<br>

조건
* 풀이시간: 30분
* 시간제한: 1초
* 메모리제한: 128MB
* 기출: Facebook 인터뷰

1. 내가 푼 것 - 틀림
~~~python
string = input()
list_string = list(string)
int_string = list(map(int, list_string))
sum, cnt = 1, 1

for i, j in zip(int_string, int_string[1:]):
    if i == 0 and i == 1:
        if cnt == 1:
            sum = i+j
            cnt += 1
        else:
            sum += j
    else:
        if cnt == 1:
            sum = i*j
            cnt += 1
        else:
            sum *= j
print(sum)
~~~

2. 강의에서 나온 것
~~~python
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 더하기를 수행
    num = int(data[i])
    if num <=1 or result <=1:
        result