"""
but i think degree is legical, howit wrong?  
10 and 10 with connected, result is 19, and 10 with 10 inconnected, 
will be 10+10 20, but 10 we take first would be the first situation one, 
so we could get wrong result

"""
from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        """
        cheak reation ship-> point to  both set 


        get top two connected city (but they should be connected and top two city)

        for road again


        plus both
        """
        #Each pair of cities has at most one road connecting them.
        #network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.
        #we have a situation that two city dont connected
        point=defaultdict(list)
        for a,b in roads:
            point[a].append(b)
            point[b].append(a)
        top=0
        for a in point.keys():
            for b in point.keys():
                if a==b:
                    continue
                if b in point[a]:
                    top=max(top,len(point[a])+len(point[b])-1)
                else:
                    top=max(top,len(point[a])+len(point[b]))
        return top

penter=Solution()
a=8
b=[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(penter.maximalNetworkRank(a,b))