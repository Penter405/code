# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        range=list()
        def recursion(root):
            if root==None:
                return 0
            recursion(root.left)
            range.append(root.val)
            recursion(root.right)
        recursion(root)
        return range[k-1]
