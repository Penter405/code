class Solution(object):
    def __init__(self):
        self.result=0
        self.target=0
        self.to_see=list()
        self.sizeof=0
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
        