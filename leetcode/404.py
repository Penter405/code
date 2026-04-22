# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #if leave means no child, and we gonna collect all not at right
        result=0
        def recursion(root, is_left):
            nonlocal result
            if root==None:
                return 0
            if root.left==None and root.right==None:
                if is_left:
                    result+=(root.val)
                return 0
            #now has at least one child
            recursion(root.left,1)
            recursion(root.right,0)
        if root==None:
            return result
        recursion(root,0)    
        return result