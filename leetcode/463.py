class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ever_seem=dict()
        total=0
        def recursion(y,x):
            nonlocal total, ever_seem,grid
            if((y,x) in ever_seem):
                return 0
            if( not(0<=y<len(grid) and 0<=x<len(grid[0]))):
                return -1
            ever_seem[(y,x)]=1
            if(grid[y][x]==0):
                return 0#me = 0
            #print("doing")
            me=4
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (y+a,x+b) in ever_seem:
                        me-=1
                elif (0<=y+a<len(grid) and 0<=x+b<len(grid[0]) and grid[y+a][x+b]==1):
                    recursion(y+a,x+b)
                    me-=1
            #print(f"piece {y} {x} is 1, his line is {me}")
            total+=me


            return 1
        for r in range(len(grid)):
            for s in range(len(grid[0])):
                if grid[r][s]!=0:
                    #print("seeing" ,r,s)
                    recursion(r,s)
                    return total
        
            
#version 2 below
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        ever_seem=dict()
        take_off=defaultdict(int)
        total=0
        def recursion(y,x):
            nonlocal total, ever_seem
            if((y,x) in ever_seem):
                return 0
            if( not(0<=y<len(grid) and 0<=x<len(grid[0]))):
                return -1
            ever_seem[(y,x)]=1
            if(grid[y][x]==0):
                return 0#me = 0
            #print("doing")
            #print(total, "+4")
            total+=4
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<=y+a<len(grid) and 0<=x+b<len(grid[0]):
                    take_off[(y+a,x+b)]+=1
                    #print(take_off)
                    recursion(y+a,x+b)
            #print(f"piece {y} {x} is 1, his line is {me}")
            return 1
        bot=0
        for r in range(len(grid)):
            if bot==1:
                break
            for s in range(len(grid[0])):
                if grid[r][s]!=0:
                    #print("seeing" ,r,s)
                    recursion(r,s)
                    bot=1
                    break
        
        for r,s in take_off:
            if grid[r][s]==1:
                total-=take_off[(r,s)]
        return total
        
            
        