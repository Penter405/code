class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[1,1]
        for rs in range(2,n+1):
            dp.append(dp[rs-2]+dp[rs-1])
        return dp[n]