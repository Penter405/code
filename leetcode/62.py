class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        my path=get top 2 legal(legal child + legal child,1)
        """

        dp=[[0]*n for _ in range(m)]


        for row in range(m):
            for column in range(n):
                if row==0 and column==0:
                    dp[row][column]=1
                elif row==0:
                    dp[row][column]=dp[row][column-1]
                elif column==0:
                    dp[row][column]=dp[row-1][column]
                else:
                    dp[row][column]=dp[row][column-1]+dp[row-1][column]
        return dp[-1][-1]
