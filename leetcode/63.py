class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        children=list()
        rows=len(obstacleGrid)
        columns=len(obstacleGrid[0])
        dp=[[0]*columns for _ in range(rows)]
        def cin(row,column):
            if row<0 or column<0:
                return 0
            if obstacleGrid[row][column]==1:
                return 0
            children.append(dp[row][column])
        for row in range(rows):
            for column in range(columns):
                if obstacleGrid[row][column]==1:
                    continue
                if row==0 and column==0:
                    dp[row][column]=1
                    continue
                children.clear()
                for a,b in [(-1,0),(0,-1)]:
                    cin(row+a,column+b)
                dp[row][column]=sum(children)
        return dp[-1][-1]