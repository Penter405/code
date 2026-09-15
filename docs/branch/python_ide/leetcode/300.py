class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp=[]
        for me in nums:
            best=0
            for i in range(len(dp)):
                if dp[i]>best and nums[i]<me:
                    best=dp[i]
            dp.append(1+best)
        
        return max(dp)

Penter=Solution()
data=[0,1,0,3,2,3]
print(Penter.lengthOfLIS(data))