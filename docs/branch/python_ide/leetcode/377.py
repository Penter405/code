class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp=[1]
        for rs in range(1,target+1):
            child=[]
            for far in nums:
                if rs-far>=0:
                    child.append(dp[rs-far])
            dp.append(sum(child))
        
        return dp[-1]