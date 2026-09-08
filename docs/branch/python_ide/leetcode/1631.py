import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        see=[(0,(0,0))]
        result={}
        while see:
            weight,place =heapq.heappop(see)
            if place in result:
                continue

            result[place]=weight

            for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0<=place[0]+a<len(heights) and 0<=place[1]+b<len(heights[0]):
                    w=abs(heights[place[0]][place[1]] -heights[place[0]+a][place[1]+b])
                    heapq.heappush(see,(max(w,weight),(place[0]+a,place[1]+b)))
        return result[(len(heights)-1,len(heights[0])-1)]

heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Penter=Solution()
print(Penter.minimumEffortPath(heights))