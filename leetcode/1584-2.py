"""
every solution we need to cheak if cycle
"""
import heapq
from collections import deque,defaultdict
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        #node=key  (time,friend) =value
        queue=[]
        for a in range(len(points)):
            for b in  range(len(points)):
                if a==b:
                    continue
                way=abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1])
                heapq.heappush(queue,(way,a,b))
        went={}
        for i in range(len(points)):
            went[i]=set([i])
        count=0
        result=0
        
        while queue:
            way,a,b=heapq.heappop(queue)
            if count==len(points)-1:
                return result
            if a in went[b] or b in went[a]:#dont know that how to cheak if should connect
                continue
            #at most one connected now
            mix=went[a].copy()
            mix.update(went[b])
            for teammate in mix:
                went[teammate]=mix
            result+=way
            count+=1
        return result
penter=Solution()
points=[[2,-3],[-17,-8],[13,8],[-17,-15]]
print(penter.minCostConnectPoints(points))