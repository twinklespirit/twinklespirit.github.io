---
################################### 게시 글 필수 정보 설정 ###################################

# 동일한 내용의 영어와 한국어 파일은 lng_pair(id)값 일치
lng_pair: id_neetcode_6
# 제목 설정 (사용 언어로 작성)
title: NeetCode 6 - Linked List
# 카테고리 설정 (1개)
category: 개인공부 
# 태그 설정 ([태그1, 태그2, ...])
tags: [leetcode, codingtest, python] 
# 저자 설정 (생략 가능) _data/owner .name 값으로 자동 설정
#author: 

# 섬네일 이미지
img: "https://user-images.githubusercontent.com/105165938/178598444-7e958a6b-a0db-4455-9707-be20b7f87ab6.png"
# 작성 날짜 설정 (YYYY-MM-DD HH:MM:SS +0900)
date: 2022-07-14 22:30:00 +0900

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
\[NeetCode\] - 6. Linked List
<!-- outline-end -->


## Problem 1. Valid Parentheses

### 1. Problem

> Given the head of a singly linked list, reverse the list, and return the reversed list.

### 2. Example and Constraints

Example 1:<br>
![img_26](https://user-images.githubusercontent.com/105165938/178829795-df07b91b-98f6-4565-9d3b-5bd26841876d.png)<br>
Input: head = [1,2,3,4,5]<br>
Output: [5,4,3,2,1]<br><br>

Example 2:<br>
![img_27](https://user-images.githubusercontent.com/105165938/178829842-6052a320-2d95-47f5-a9bf-3a62eb65cc1a.png)<br>
Input: head = [1,2]<br>
Output: [2,1]<br><br>

Example 3:<br>
Input: head = []<br>
Output: []<br><br>

Constraints:<br>
* The number of nodes in the list is the range [0, 5000].
* -5000 <= Node.val <= 5000

### 3. Solution
This is an easy problem


### 4. Coding in Python3

~~~python
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
            
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
~~~

### 5. Big O 
* Time Complexity
    * Stack operations .push() and .pop() operate on O(1)
    * loop through all elements of the list O(n)
    (the time complexity of this problem is O(n))  
* Space Complexity
    * store all the elements of the list O(n)



## Problem 2. Merge Two Sorted Lists

### 1. Problem


### 2. Example and Constraints

### 3. Solution

### 4. Coding in Python3

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1st1 and list2:
            if list1.val < list2.val:
                tail.next = 11
                list1 = list1.next
            else:
                tail.next = 12
                list1 = list1.next
            tail = tail.next
        return dummy.next
~~~

### 5. Big O



## Problem 3. Longest Repeating Character Replacement (Medium)

### 1. Problem

### 2. Example and Constraints

### 3. Solution

### 4. Coding in Python3

~~~python

~~~

### 5. Big O 
### 1. Problem

### 2. Example and Constraints

### 3. Solution

### 4. Coding in Python3

~~~python

~~~

### 5. Big O



## Problem 4. Permutation in String (Medium)

### 1. Problem

### 2. Example and Constraints

### 3. Solution

### 4. Coding in Python3

~~~python

~~~

### 5. Big O



## Problem 5. Minimum Window Substring (Hard)

### 1. Problem

### 2. Example and Constraints

### 3. Solution

### 4. Coding in Python3

~~~python

~~~

### 5. Big O




## Problem 6. Sliding Window Maximum (Hard)

### 1. Problem

### 2. Example and Constraints

### 3. Solution

### 4. Coding in Python3

~~~python

~~~

### 5. Big O


