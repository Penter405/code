# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #ranges=list()
        def recursion(root):
            if root==None:
                return 0
            bot=root.left
            root.left=root.right
            root.right=bot
            recursion(root.right)
            recursion(root.left)
        recursion(root)
        return root  