# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 해결법
# 트리는 전위, 중위, 후위 순회 중 2개만 있어도 이진트리로 구현이 가능함.
# why? 
# 전위(N,L,R)에서 N은 중위(L,N,R)의 N과 같다. 그러니깐, 전위 순회의 첫 번째 요소로 중위 순회의 결과를 정확히 반으로 분할할 수 있다는 것이다.
# 이를 Divide and Conquer라고 한다.


class Solution:

    def buildTree(self, preorder, inorder):
        if inorder: 
            # 전위 순회 결과 첫번째 값을 이용하여 == 중위 순회 결과 중앙값의 인덱스를 찾는다. (to divide)
            # 1. pop(0) O(n)
            # 2. index(val) O(1) why? (1) 인덱스로 접근 (2) 인덱스 안에 있는 데이터를 읽기 (2번 기본 연산)
            index = inorder.index(preorder.pop(0))
            
            # 
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])
            
            return node


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]


a = Solution()
#print(a.buildTree(preorder, inorder).left)
print(a.buildTree(preorder, inorder).val)
#print(a.buildTree(preorder, inorder).right)