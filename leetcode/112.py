# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        is_same=False
        def recursion(root,count):
            nonlocal is_same
            if is_same or root==None:
                return 0
            count+=root.val
            if root.left==None and root.right==None:
                if count==targetSum:
                    is_same=True
                return 0
            recursion(root.left,count)
            recursion(root.right,count)
        recursion(root,0)
        return is_same