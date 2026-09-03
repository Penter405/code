from functools import cache


class Solution(object):
    def __init__(self):
        self.result=0
        self.target=0
        self.to_see=list()
        self.sizeof=0
    @cache
    def recursion(self,back_pointer,total):
        if back_pointer==self.sizeof:
            #do add result;
            if total==self.target:
                self.result+=1
            return 0
        buffer=self.to_see[back_pointer]
        self.recursion(back_pointer+1,total+buffer)
        self.recursion(back_pointer+1,total-buffer)
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.to_see=nums
        self.target=target
        self.sizeof=len(nums)
        self.recursion(0,0)
        return self.result
        
#version two, still fail
#from functools import cache
result=0
def recursion(back_pointer,total,sizeof,target,to_see):
    global result
    if back_pointer==sizeof:
        #do add result;
        if total==target:
            result+=1
        return 0
    buffer=to_see[back_pointer]
    recursion(back_pointer+1,total+buffer,sizeof,target,to_see)
    recursion(back_pointer+1,total-buffer,sizeof,target,to_see)
class Solution(object):
    def __init__(self):
        self.result=0
        self.target=0
        self.to_see=list()
        self.sizeof=0
    
    
    def findTargetSumWays(self, nums, target):
        global result
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.to_see=nums
        self.target=target
        self.sizeof=len(nums)
        recursion(0,0,self.sizeof,self.target,self.to_see)
        return result
#node below
"""
i was facing TLE
so we can dp or cashe,
but what is cashe?
"""