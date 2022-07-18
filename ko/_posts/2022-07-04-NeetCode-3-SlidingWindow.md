---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_neetcode_3
# 제목 설정 (사용 언어로 작성)
title: NeetCode 3 - Sliding Window
# 카테고리 설정 (1개)
category: 개인공부
# 태그 설정 ([태그1, 태그2, ...])
tags: [leetcode, codingtest, python] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/178598444-7e958a6b-a0db-4455-9707-be20b7f87ab6.png"
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-08 21:00:00 +0900

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
\[NeetCode\] - 3. Sliding Window
<!-- outline-end -->

슬라이딩 윈도우란?
고정 사이즈의 윈도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 풀이하는 알고리즘을 말한다.
배열이나 리스트의 요소의 일정 범위의 값을 비교할 대 사용하면 매우 유용하다. 원래 네트워크에서 사용되던 알고리즘을 문제풀이에 응용한 것이라고 할 수 있다.


## Problem 1. Best Time to Buy & Sell Stock (Easy)
### 1. Problem
> You are given an array prices where prices\[i\] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://www.youtube.com/watch?v=uH9VJRIpIDY

### 2. Solution
Example 1:<br>
Input: prices = \[7,1,5,3,6,4\]<br>
Output: 5
Explanation: Buy on day 2 and sell on day 5, profit is 5.

* 필요한 변수
    * buy: 배열에서 최소값
    * sell: buy 이후의 수 중 최대값
    * profit: 0 혹은 buy-sell

* 문제를 해결해보자!
\[0\] 

### 3. Coding in Python3
~~~python
class Solution:
    def maxProfit(selt, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
~~~

## Problem 2. Longest Substring Without Repeating Characters (Medium)

## Problem 3. Longest Repeating Character Replacement (Medium)
### 1. Problem
> You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

 ### 2. Solution
 

 ### 3. Coding

## Problem 4. Permutation in String (Medium)

## Problem 5. Minimum Window Substring (Hard)

## Problem 6. Sliding Window Maximum (Hard)
