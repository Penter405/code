#attempted by did not cheak cycle
import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        #node=key  (time,friend) =value
        queue2=[]
        for a in range(len(points)):
            for b in  range(len(points)):
                if a==b:
                    continue
                way=abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1])
                heapq.heappush(queue2,(way,a,b))
        went=set()
        count=0
        result=0
        queue=[heapq.heappop(queue2)]
        while queue:
            way,a,b=heapq.heappop(queue)
            if count==len(points):
                return result
            if tuple(sorted((a,b))) in went:#dont know that how to cheak if should connect
                continue
            #at most one connected now
            went.add(tuple(sorted((a,b))))
            result+=way
            count+=1
penter=Solution()
points=[[2,-3],[-17,-8],[13,8],[-17,-15]]
print(penter.minCostConnectPoints(points))