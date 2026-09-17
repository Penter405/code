#attpemted, Time out
import heapq
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        #weighted bfs
        m=len(grid)
        n=len(grid[0])
        cheaked=dict()
        queue=[]
        #heappush
        #heappop
        #down or right
        heapq.heappush( queue , (grid[0][0],(0,0)))
        while (m-1,n-1) not in cheaked:
            got,place=heapq.heappop(queue)
            cheaked[place]=got
            for a,b in [(0,1) , (1,0) ]:
                if 0<= place[0]+a <m and 0<= place[1]+b <n:
                    heapq.heappush( queue,  (got+grid[place[0]+a][place[1]+b] ,  (place[0]+a,place[1]+b) )   )
            
        return cheaked[(m-1,n-1)]