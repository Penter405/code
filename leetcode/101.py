# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        r_list=list()
        l_list=list()
        def r_first(root):
            nonlocal r_list
            if root==None:
                r_list.append(-1)
                return 0
            r_list.append(root.val)
            r_first(root.right)
            r_first(root.left)
        def l_first(root):
            nonlocal l_list
            if root==None:
                l_list.append(-1)
                return 0
            l_list.append(root.val)
            l_first(root.left)
            l_first(root.right)
        r_first(root)
        l_first(root)
        return r_list==l_list