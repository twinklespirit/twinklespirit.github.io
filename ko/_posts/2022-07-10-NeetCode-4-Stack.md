---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_leetcode
# 제목 설정 (사용 언어로 작성)
title: leetcode Vaild Palindrome - 4. Stack
# 카테고리 설정 (1개)
category: 취업준비 
# 태그 설정 ([태그1, 태그2, ...])
tags: [leetcode] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img:  
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-10 10:30:00 +0900

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
\[NeetCode\] - 4. Stack
<!-- outline-end -->


## Problem 1. Valid Parentheses
### 1. Problem
> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. <br> An input string is valid if:<br>   1. Open brackets must be closed by the same type of brackets.<br>   2. Open brackets must be closed in the correct order.

### 2. Example and Constraints
Example 1:<br>
Input: s = "()"<br>
Output: true<br><br>

Example 2:<br>
Input: s = "()[]{}"<br>
Output: true<br><br>

Example 2:<br>
Input: s = "(]"<br>
Output: false<br><br>

Constraints:<br>
* 1 <= s.length <= 104
* s consists of parentheses only '()[]{}'

### 3. Solution
First, let me summarize. 
1. when \(, \[, \{ is entered, push them onto the stack and # when이 맞아요? if가 맞아요?
2. when \), \], \} is entered, pop
3. Check that the result matches the mapping table result.
    * (A) mapping table: (is) a dictionary data structure made up of keys and values.
    * We remove the character inserted into the list if it is the same as the key of the table.
    * We will compare the remaining character in the list with the value that correspond to key in the table.
    1. Create the mapping table and
    2. pushes it unconditionally if it does not exist in the table and
    3. returns False if the result does not match when popped.

### 4. Coding in Python3
~~~python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            # if there is no char in table
            if char not in table:
                # append char in stack
                stack.append(char)
            # the char is on the table so remove it
            # and 
            elif not stack or table[char] != stack.pop():
                # return False
                return False
        
        # 예외 처리: 예를들어 '['가 입력될 때도 true를 출력해 줘야 함
        return len(stack) == 0 # Return True if the stack length is 0
~~~

### 5. Big O
* Time Complexity
    * Stack operations .push() and .pop() operate on O(1)
    * 

## Problem 2. Longest Substring Without Repeating Characters (Medium)

## Problem 3. Longest Repeating Character Replacement (Medium)
### 1. Problem
> You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

 ### 2. Solution
 

 ### 3. Coding

## Problem 4. Permutation in String (Medium)

## Problem 5. Minimum Window Substring (Hard)

## Problem 6. Sliding Window Maximum (Hard)
