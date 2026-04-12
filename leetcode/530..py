# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.data=list()
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def recursion(root):
            if(root.left):
                recursion(root.left)
            self.data.append(root.val)
            if(root.right):
                recursion(root.right)
        recursion(root)
        #self.data.sort()//get it
        print(self.data)
        result=-1
        for i in range(len(self.data)-1):
            if result==-1 or self.data[i+1]-self.data[i]<result:
                result=self.data[i+1]-self.data[i]
        return result