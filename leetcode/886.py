#time costed is 0:15:02
from collections import defaultdict,deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        point=defaultdict(list)

        for a,b in dislikes:
            point[a].append(b)
            point[b].append(a)
        
        state=[0]*(n+1)

        cheaked=[0]*(n+1)
        legal=True
        def bfs(me):
            nonlocal state,cheaked,legal
            queue=deque()
            queue.append(me)
            if state[me]==0:
                state[me]=1
            while queue:
                node=queue.popleft()
                if cheaked[node]==1:
                    continue
                cheaked[node]=1
                for neighbor in point[node]:
                    if state[neighbor]==0:
                        state[neighbor]=-state[node]
                    else:
                        if state[neighbor]==state[node]:
                            legal=False
                            return False
                    if cheaked[neighbor]==0:
                        queue.append(neighbor)
            return True
        for node in range(1,n+1):
            if bfs(node)==False:
                return False
        return True

            

Penter=Solution()
n=10
dislikes=[[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
print(Penter.possibleBipartition(n, dislikes))