#version 2(new version)
class Solution:
    def recursion(self, grid,index_first,index_second)->int:
        if((not (0<=index_first<len(grid))) or not(0<=index_second< len(grid[0]) ) ):
            return 0
        if(grid[index_first][index_second]==0):
            return 0
        me=grid[index_first][index_second]
        #print("recursion",me)
        grid[index_first][index_second]=0
        buffer=0
        for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
            buffer+=self.recursion(grid,index_first+a,index_second+b)
        
        return me+buffer
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        result=0
        for f in range(len(grid)):
            for s in range(len(grid[0])):
                if grid[f][s]!=0:
                    bot=self.recursion(grid, f, s)
                    #print(bot)
                    if(bot%k==0):
                        result+=1
        
        return result





#version 1
class Solution:
    def recursion(self, grid,index_first,index_second)->int:
        if((not (0<=index_first<len(grid))) or not(0<=index_second< len(grid[0]) ) ):
            return 0
        if(grid[index_first][index_second]==0):
            return 0
        me=grid[index_first][index_second]
        #print("recursion",me)
        grid[index_first][index_second]=0
        a=self.recursion(grid,index_first+1,index_second)
        b=self.recursion(grid,index_first-1,index_second)
        c=self.recursion(grid,index_first,index_second+1)
        d=self.recursion(grid,index_first,index_second-1)
        return me+a+b+c+d
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        result=0
        for f in range(len(grid)):
            for s in range(len(grid[0])):
                if grid[f][s]!=0:
                    bot=self.recursion(grid, f, s)
                    #print(bot)
                    if(bot%k==0):
                        result+=1
        
        return result
        