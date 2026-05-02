class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def recursion(y,x):
            nonlocal grid
            if not(0<=y<len(grid) and 0<=x<len(grid[0])):
                return 0
            if grid[y][x]==0:
                return 0
            me=grid[y][x]
            grid[y][x]=0
            a=recursion(y+1,x)
            b=recursion(y-1,x)
            c=recursion(y,x+1)
            d=recursion(y,x-1)
            return me+a+b+c+d
        result=0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]!=0:
                    bot=recursion(y,x)
                    if bot>result:
                        result=bot
        return result