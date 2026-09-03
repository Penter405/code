#too slow,  9000 ms
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        done=set()
        point=defaultdict(list)
        for a,b in edges:
            point[a].append(b)
            point[b].append(a)
        
        result=defaultdict(list)
        time=-1
        while len(done)<n:
            time+=1
            for me in range(n):
                if me in done:#o(log 2 to n) in bst or o(1) in hash
                    continue
                if len(point[me])<=1:
                    result[time].append(me)
                    done.add(me)

            for me in result[time]:
                for take in point[me]:
                    point[take].remove(me)#o(n)
                point[me].clear()
        return result[time]

Penter=Solution()
a=4
b=[[1,0],[1,2],[1,3]]
Penter.findMinHeightTrees(a,b)