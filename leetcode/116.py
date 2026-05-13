"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def recursion(self,root):
        if(root):
            print(root.val)
            self.recursion(root.next)
        else:
            print("im none")
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.recursion(root)
        return root
    #the next is default in none.
    #right root left search