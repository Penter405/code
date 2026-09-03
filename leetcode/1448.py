# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result=0
        def recursion(root,most_ever:int):
            nonlocal result
            if root==None:
                return 0
            if root.val>=most_ever:
                most_ever=root.val
                result+=1
            recursion(root.left,most_ever)
            recursion(root.right,most_ever)

        recursion(root,root.val)
        return result