"""
failed degree that pretend that max value one(if we have many max value node) will be the answer (see row 31)
see more info in 1615-2.py
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
        top=-1
        guy1=-1
        got=-1
        got2=-1
        for me in point.keys():#fail degree
            if len(point[me])>got:
                guy1=me
                got=len(point[me])
        for me in point.keys():
            if me==guy1:#there is a statu that two point same value
                continue
            if len(point[me])>got2:
                if guy1 in point[me]:
                    top=max(top,got+len(point[me])-1)
                else:
                    top=max(top,got+len(point[me]))
        return top

penter=Solution()
a=8
b=[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(penter.maximalNetworkRank(a,b))