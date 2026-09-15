class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0,0]
        for rs in range(2,len(cost)+1):
            dp.append(min(      (cost[rs-1]+dp[rs-1]) ,  (cost[rs-2]+dp[rs-2])  ))
        return dp[-1]