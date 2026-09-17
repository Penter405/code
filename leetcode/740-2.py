class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        point=[0]*(max(nums)+1)
        for element in nums:
            point[element]+=element
        
        def get(n):
            if n<0:
                return 0
            return dp[n]
        dp=[0]*(max(nums)+1)
        
        for guy,money in enumerate(point):
            dp[guy]=max(  get(guy-1),  get(guy-2) +  money )
        return max(dp)