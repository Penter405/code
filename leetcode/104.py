# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        big=0
        #is immutable object in parameter change?, no ,always different object if edit
        def recur(root,depth):
            nonlocal big
            if root==None:
                return 0
            if depth>big:
                big=depth
            if root.left:
                recur(root.left,depth+1)
            if root.right:
                recur(root.right,depth+1)
        recur(root,1)
        return big