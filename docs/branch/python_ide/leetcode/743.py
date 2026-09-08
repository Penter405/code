import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        point=defaultdict(list)
        
        for sub, obj,weight in times:
            point[sub].append((weight,obj))
        went={}
        queue=[(0,k)]#put went path weight in this queue, so heappop will compare all leave(the path that child has not been called) and get the minimum one
        while queue:
            weight,me=heapq.heappop(queue)
            if me in went:
                continue
            went[me]=weight#minimum one did not puted in, so we put
            for weight,child in point[me]:
                heapq.heappush(queue,(went[me]+weight,child))

        if len(went)!=n:
            return -1
        return max(went.values())


Penter=Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]; n = 4; k = 2
print(Penter.networkDelayTime(times,n,k))
