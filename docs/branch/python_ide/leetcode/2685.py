from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        path between any two vertices=all connected 
        """
        point=defaultdict(list)#undirected
        #pointed=defualtdict(list)

        for a,b in edges:
            point[a].append(b)
            point[b].append(a)
        
        went=set()
        result=0
        def make(me):
            guys=[]
            def dfs(me):
                nonlocal guys,went
                if me in went:
                    return 0
                went.add(me)
                guys.append(me)
                #print(me)
                for child in point[me]:
                    dfs(child)
                return 0

            dfs(me)
            #print(guys)
            if len(guys)==0:
                return 0
            for rs in guys:
                if len(point[rs])!=len(guys)-1:
                    return 0
            return 1
        for node in range(n):
            result+=make(node)
        return result

