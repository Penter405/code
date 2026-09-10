#cost 0:13:50 time
from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        went=[0]*len(graph)
        went[0]=1
        
        legal=True
        cheaked=set()
        def bfs(me):
            nonlocal legal
            went=[0]*len(graph)
            went[me]=1
            queue=deque()
            queue.append(me)

            while queue:
                node=queue.popleft()
                if node in cheaked:
                    continue
                cheaked.add(node)
                for neighbor in graph[node]:
                    if went[neighbor]==0:
                        went[neighbor]=-(went[node])
                    else:
                        if went[node]==went[neighbor]:
                            legal=False
                            return 0
                    if neighbor not in cheaked:
                        queue.append(neighbor)
            return 1
        for node in range(len(graph)):
            bfs(node)
        return legal
Penter=Solution()
graph=[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]#expect false
print(Penter.isBipartite(graph))