---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_neetcode_2
# 제목 설정 (사용 언어로 작성)
title: NeetCode 2 - Two Pointers
# 카테고리 설정 (1개)
category: 개인공부 
# 태그 설정 ([태그1, 태그2, ...])
tags: [leetcode, codingtest, python] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/178598444-7e958a6b-a0db-4455-9707-be20b7f87ab6.png"
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-06 11:00:00 +0900

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
Vaild Palindrome

## Problem 1. Valid Palindrome (Easy)
주어진 문자열이 팰린드롬인지 확인하자
* 팰린드롬: 앞뒤가 똑같은 단어나 문장 (뒤집어도 같은 말이 되는 단어 또는 문장)
* 한국말로는 '회문'

### 1. Problem 
> A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.<br> Given a string s, return true if it is a palindrome, or false otherwise.

<br><br>

### 2. Example and Constraints
Example 1:<br>
* Input: s = "A man, a plan, a canal: Panama"<br>
* Output: true<br>
* Explanation: "amanaplanacanalpanama" is a palindrome.
<br><br>

Example 2:<br>
* Input: s = "race a car"<br>
* Output: false<br>
* Explanation: "raceacar" is not a palindrome.
<br><br>
 
Example 3:<br>
* Input: s = " "<br>
* Output: true<br>
* Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
<br><br>

Constraints:
*  1 <= s.length <= 2 * 105
* s consists only of printable ASCII characters.
<br><br>

### 3. Solution
* Data processing
    1. converting all uppercase -> lowercase
    2. removing all non-alphanumeric charaters
* Solve the Problem
    1. 기존 문자열을 리스트로 준비
    2. 리스트를 뒤집어서 준비
    3. 이 두개의 리스트가 같은지 비교
<br><br>

### 4. Coding in Python3
1. 리스트 자료구조를 이용하여 문제 해결

~~~python 
# Create Class
class Solution:
    # Declare function
    def isPalindrome(self, s: str) -> bool: # input str s, return bool
        # 1. Convert all uppercase -> lowercase
        s_lower = s.lower()
        # 2. Remove all non-alphanumeric
        s_alnum = [] 
        for char in s_lower:         # 문자열을 순회하는데
            if char.isalnum():       # 만약 문자, 숫자라면 
                s_alnum.append(char) # 리스트의 요소로 추가!
        
        # 3. 
        s_reversed = s_alnum[::-1]
        if s_alnum == s_reversed:
            return true
        else:
            return false
       
~~~

2. 데크 자료형을 이용한 최적화

3. 슬라이싱 이용
<br><br>

### 5. Big O 
<br><br><br><hr>

## Problem 2. Two Sum II
### 1. Problem 
### 2. Example and Constraints
Example 1:<br>
* Input:  <br>
* Output:  <br>
* Explanation:
<br><br>
 
Constraints:
*  

### 3. Solution
### 4. Coding in Python3
~~~python 
~~~
### 5. Big O 
<br><br><br><hr>

## Problem 3. 3Sum
### 1. Problem 
### 2. Example and Constraints
Example 1:<br>
* Input:  <br>
* Output:  <br>
* Explanation:
<br><br>
 
Constraints:
*  
### 3. Solution
### 4. Coding in Python3
~~~python 
~~~
### 5. Big O 
<br><br><br><hr>

## Problem 4. Container with Most Water
### 1. Problem 
### 2. Example and Constraints
Example 1:<br>
* Input:  <br>
* Output:  <br>
* Explanation:
<br><br>
 
Constraints:
*  
### 3. Solution
### 4. Coding in Python3
~~~python 
~~~
### 5. Big O 
<br><br><br><hr>

## Problem 5. Trapping Rain Water
### 1. Problem 
### 2. Example and Constraints
Example 1:<br>
* Input:  <br>
* Output:  <br>
* Explanation:
<br><br>

Constraints:
*  
### 3. Solution
### 4. Coding in Python3
~~~python 
~~~
### 5. Big O 