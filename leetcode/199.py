# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=list()
        sizeof=-1
        def recursion(root,depth):
            nonlocal sizeof
            if root==None:
                return 0
            if depth>sizeof:
                #print(depth,"more than ",sizeof)
                sizeof=depth
                result.append(root.val)
            recursion(root.right,depth+1)
            recursion(root.left,depth+1)
        recursion(root,0)
        return result