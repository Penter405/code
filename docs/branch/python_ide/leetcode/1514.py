import heapq
from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        point=defaultdict(list)
        for i in range(len(edges)):
            point[edges[i][0]].append((succProb[i],edges[i][1]))
            point[edges[i][1]].append((succProb[i],edges[i][0]))
        
        next_=[(1,start_node)]
        went={}
        while next_:
            weight,node=heapq.heappop_max(next_)
            if node in went:
                continue
            went[node]=weight
            if node==end_node:
                return went[node]
            
            for w,child in point[node]:
                heapq.heappush_max(next_,(weight*w,child))
        
        return float(0)

Penter=Solution()
Penter.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)