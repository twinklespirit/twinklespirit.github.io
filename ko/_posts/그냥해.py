# 재귀함수 이해하기

# 1. 이거는 런타임 아웃이난다. 왜? 끝도없이 달리니깐~
#def hello():
#    print('Hello, world!')
#    hello()
 
#hello()

# 2. 팩토리얼
#def factorial(n):
#    if n == 1:      # n이 1일 때
#        return 1    # 1을 반환하고 재귀호출을 끝냄
#    return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 
#print(factorial(5))

#def recursive_call(x):
#    print(x)
#    recursive_call(x+1)
    
#recursive_call(1)

#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

#a = TreeNode(1)
#print(a.val)
#print(a.left)
#print(a.right)

#a = [1,2,3,4,5]
#print(a[0:0])

inorder = [9,3,15,20,7]
preorder = [3,9,20,15,7]

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def buildTree(self, preorder, inorder):

        global node

        if inorder: 
            index = inorder.index(preorder.pop(0))
            print(index, end=" ")
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

        return node

a = Solution()
print(a.buildTree(preorder, inorder))