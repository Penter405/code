# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #unknown order traval
        #traval by left to right, up to down
        #it seems like inorder traval with spilt with something
        #go child = up_down +1
        #left=left_right-1
        #right=left_right+1
        result=list()
        same_index:dict[tuple, list]=dict()
        #def initialize_same_index(,):
        def recursion(root,left_right:int,up_down:int):
            nonlocal result ,same_index
            if root==None:
                return 0
            recursion(root.left,left_right-1,up_down+1)
            #----------
            #add self into


            if (left_right,up_down) in same_index:
                same_index[(left_right,up_down)].append(root.val)
            else:
                same_index[(left_right,up_down)]=[root.val]
            
            

            #----------
            recursion(root.right,left_right+1,up_down+1)

        recursion(root,0,0)
        print(same_index)
        #after recursion, the sorted order of dictionary same_index will must be left right first , and then up down first
        last_left_right=None
        for rs in sorted(same_index.keys()):
            if last_left_right!=rs[0]:
                last_left_right=rs[0]
                result.append(list())
            result[-1].extend(sorted(same_index[rs]))

        return result