class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        #islnd= land connect recursion its left, right top, bottom land, not include out of index
        #land is 0 , hmm, return 0 as land
        row_size=len(grid)
        column_size=len(grid[0])
        ever=set()
        result=0
        any_bad=0

        def is_water(row,column):
            nonlocal grid,any_bad
            if row==0 or row==row_size-1 or column==0 or column==column_size-1:
                if grid[row][column]==0:
                    any_bad=1

            if 0<row<row_size-1 and 0<column<column_size-1:
                return grid[row][column]
            else:
                return 1
        def recursion(row,column):
            nonlocal grid
            if is_water(row,column):
                return 0
            if (row,column) in ever:
                return 0
            ever.add((row,column))
            for a,b in [(0,-1),(0,1),(1,0),(-1,0)]:
                recursion(row+a,column+b)
        
        for rs in range(row_size):
            for pe in range(column_size):
                if not is_water(rs,pe) and (rs,pe) not in ever:
                    any_bad=0
                    recursion(rs,pe)
                    if any_bad==0:
                        result+=1
        return result
