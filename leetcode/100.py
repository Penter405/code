# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result=1
        def recursion(root,root2):
            nonlocal result
            if root==None:
                if root2==None:
                    pass
                else:
                    result=0
                return 0
            if root2==None:
                if root==None:
                    pass
                else:
                    result=0
                return 0
            if root.val!=root2.val:
                result=0
            recursion(root.left,root2.left)
            recursion(root.right,root2.right)
        recursion(p,q)
        return bool(result)