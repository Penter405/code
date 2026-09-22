"""
situation: if give x have money, give x+2 money -> x have money, we was seeing x, x+2 must got money, and then we see x+2, give x+4 money, 
solution: when x+2 have momey, x should have money
"""
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        part=sum(nums)//2
        
        dp=[0]*part+[1]

        for guy in nums:
            for place in range(len(dp)):
                if not(0<=place+guy<=len(dp)-1):
                    continue
                if dp[place+guy]==1:
                    dp[place]=1
        
        return bool(dp[0])