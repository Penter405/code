# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #preorder -> root first
        result=[]
        def recur(root):
            nonlocal result
            if root==None:
                return 0
            result.append(root.val)
            if root.left:
                recur(root.left)
            if root.right:
                recur(root.right)
        recur(root)
        #print(result)
        return result