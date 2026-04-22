# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result=0
        def recursion(root,count):
            nonlocal result
            if root==None:
                return 0
            count=count*10+root.val
            if root.left==None and root.right==None:
                result+=count
                return 0
            recursion(root.left,count)
            recursion(root.right,count)
        recursion(root,0)
        return result