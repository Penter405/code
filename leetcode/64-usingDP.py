class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        #weighted bfs
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]

        #heappush
        #heappop
        #down or right
        def get(row,column):
            if 0<=row<m and 0<=column<n:
                return dp[row][column]
            return -1
        def find_min(*guys):
            mymin=-1
            for guy in guys:
                if guy!=-1 and (mymin==-1 or guy<mymin):
                    mymin=guy
            return mymin
        for row in range(m):
            for column in range(n):
                child=find_min(get(row-1,column), get(row,column-1))
                if child==-1:
                    dp[row][column]=grid[row][column]
                else:
                    dp[row][column]=grid[row][column]+child
            
            
        return dp[-1][-1]

penter=Solution()
grid=[[1,3,1],[1,5,1],[4,2,1]]
print(penter.minPathSum(grid))