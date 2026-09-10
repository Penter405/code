import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        parent=[i for i in range(len(points))]
        def find(me):
            if parent[me]==me:
                return me
            return find(parent[me])
        def union(a,b):
            root_a=find(a)
            root_b=find(b)
            
            if root_a==root_b:
                return False
            parent[root_b]=root_a

            return True

        result=0
        count=0
        queue=[]
        for a in range(len(points)):
            for b in range(len(points)):
                if a==b:
                    continue
                t=abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1])
                heapq.heappush(queue,(t,(a,b)))
        while queue:
            weight,point=heapq.heappop(queue)
            if count==len(points)-1:
                return result
            if union(point[0],point[1]):
                result+=weight
                count+=1
        return result

