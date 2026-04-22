# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def the_min(a,b):
            if a==0:
                return b
            if b==0:
                return a
            return min(a,b)
        def recursion(root,depth):
            if root==None:
                return 0
            if root.left==None and root.right==None:
                return depth
            return the_min(recursion(root.left,depth+1),recursion(root.right,depth+1))
        return recursion(root,1)

#version two below
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        result=-1
        #do boarden search first
        stack=[[root,1]]
        now_index=0
        while stack:
            
            if stack[now_index][0]==None:
                pass
            elif stack[now_index][0].left==None and stack[now_index][0].right==None:
                break
            else:
                #print("seeing", stack[now_index][0].val)
                #go on
                stack.append([stack[now_index][0].left,stack[now_index][1]+1])
                stack.append([stack[now_index][0].right,stack[now_index][1]+1])
            #print("add")
            now_index+=1
        return stack[now_index][1]