#0:37:31 times
class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        """
        top 1
        bottom -1
        left 2
        right -2
        """
        ever=set()
        legal=0
        max_row=len(grid)
        max_column=len(grid[0])
        represent={
            1:[2,-2],
            2:[1,-1],
            3:[2,-1],
            4:[-2,-1],
            5:[1,2],
            6:[1,-2]
        }
        def dfs(row=0,column=0,dad_side=None):
            nonlocal legal
            if legal==1:
                return 0
            if not (0<=row<max_row and 0<=column<max_column):
                return 0
            
            if (row,column) in ever:
                return 0
            ever.add((row,column))
            if dad_side==None or -(dad_side) in represent[grid[row][column]]:
                if row== max_row-1 and column==max_column-1:
                                legal=1
                                return 0
                for rs in represent[grid[row][column]]:
                    if rs==1:
                        dfs(row-1,column,1)
                    elif rs==-1:
                        dfs(row+1,column,-1)
                    elif rs==2:
                        dfs(row,column-1,2)
                    elif rs==-2:
                        dfs(row,column+1,-2)
        dfs()
        return bool(legal)
data=[[2],[4]]
penter=Solution()
print(penter.hasValidPath(data))
