
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ranger=list()
        def recursion(root):
            if root==None:
                return 0
            recursion(root.left)
            ranger.append(root.val)
            recursion(root.right)
        recursion(root)
        for i in range(len(ranger)-1):
            if ranger[i]>=ranger[i+1]:
                return False
        return True