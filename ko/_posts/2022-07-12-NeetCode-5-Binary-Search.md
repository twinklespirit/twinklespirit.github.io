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
date: 2022-07-12 10:30:00 +0900

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
\[NeetCode\] - 5. Binary Search
<!-- outline-end -->


## Problem 1. Valid Parentheses
### 1. Problem
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
        # declare a list named "stack" which provides operations available on stack
        stack = [] # storing elements in order (dynamic array)
        # create a function named "mapping table" which compares characters inputed to keys
        mapping_table = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        # loop through the string named "s" by using a for loop
        for bracket in s:
            # if there is no bracket in table(key: '), }, ]')
            if bracket not in table:
                # append brackets in stack
                stack.append(bracket)
            # the bracket is on the table
            # compare bracket to value correspond to key 
            # if not the same
            elif not stack or table[bracket] != stack.pop():
                # return False
                return False
        
        # exception handling: 예를들어 '['가 입력될 때도 true를 출력해 줘야 함
        return len(stack) == 0 # Return True if the stack length is 0
~~~

### 5. Big O 
* Time Complexity
    * Stack operations .push() and .pop() operate on O(1)
    * loop through all elements of the list O(n)
    (the time complexity of this problem is O(n))  
* Space Complexity
    * store all the elements of the list O(n)

## Problem 2. Longest Substring Without Repeating Characters (Medium)

## Problem 3. Longest Repeating Character Replacement (Medium)
### 1. Problem
> There are n cars going to the same destination along a one-lane road. The destination is target miles away. <br>
> You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour). <br>
> A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position). <br>
> A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet. <br>
> If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet. <br>
> Return the number of car fleets that will arrive at the destination.

### 2. Example and Constraints
Example 1:<br>
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]<br>
Output: 3<br>
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.<br><br>

Example 2:<br>
Input: target = 10, position = [3], speed = [3]<br>
Output: 1<br>
Explanation: There is only one car, hence there is only one fleet.<br><br>

Example 3:<br>
Input: target = 100, position = [0,2,4], speed = [4,2,1]<br>
Output: 1<br>
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.<br><br>

Constraints:
* n == position.length == speed.length
* 1 <= n <= 105
* 0 < target <= 106
* 0 <= position[i] < target
* All the values of position are unique.
* 0 < speed[i] <= 106

### 3. Solution
1. 자동차의 위치를 정렬 (named cars)
2. 자동차의 위치에서 목적지까지 가는 **시간**을 구한다. (시간=거리/속력)
3. cars 위치가 [5,3]-> (X), [3,3]-> (O) 따라 잡을 순 없고 같이 갈 순 있음
4. 

### 4. Coding in Python3
~~~python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (1) zip
        # (2) sorted by position
        cars = sorted(zip(position, speed))
        # time = distance/speed
        times = [(target-p)/s for p, s in cars]
        # 전부다 똑같이 들어올 경우
        fleet = 1
        # stack 연산을 이용하여 마지막 요소를 하나씩 제거하며 비교
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                fleet += 1
            else:
                times[-1] = lead
        return fleet
~~~

### 5. Big O 

## Problem 4. Permutation in String (Medium)

## Problem 5. Minimum Window Substring (Hard)

## Problem 6. Sliding Window Maximum (Hard)

## Problem 8. Find Median of Two Sorted Arrays (Hard)
### 1. Problem
> Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.<br> The overall run time complexity should be O(log (m+n)).

### 2. Example and Constraints
Example 1:<br>
* Input: nums1 = [1,3], nums2 = [2]
* Output: 2.00000
* Explanation: merged array = [1,2,3] and median is 2.<br><br>


Example 2:<br>
* Input: nums1 = [1,2], nums2 = [3,4]
* Output: 2.50000
* Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.<br><br>

Constraints:<br>
* nums1.length == m
* nums2.length == n
* 0 <= m <= 1000
* 0 <= n <= 1000
* 1 <= m + n <= 2000
* -106 <= nums1[i], nums2[i] <= 106

### 3. Solution
To solve the problem, understanding the nature of the median is very important. One of the characteristics of the median is that dividing a set into two sets, the set of lower elements, the set of higher elements. 
<br>
Each array has elements included a lower set or higher set simultaneously like this. 
<br>
left_part is the lower element set and right_part is the higher element set. Using this feature, we can deduce the following formula
<br>
left_part's size and right_part's size are equal. There is no doubt. The second formula is obvious because left_part's elements are always less than the right_part's
<br>


### 4. Coding in Python3
~~~python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        # 1. sort two list
         merged_mn = nums1 + nums2
         sorted_mn = merged_mn.sort()
         # 2. check the len of sorted_mn
         len_mn = len(len_mn)
         # 3. center value
         center = sorted_mn(len_mn)


~~~
### 5. Big O 