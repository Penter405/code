class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        parent=[a for a in range(len(isConnected))]
        rank=[1 for _ in range(len(isConnected))]
        result=len(isConnected)
        def find(me):
            if parent[me]==me:
                return me
            return find(parent[me])
        def union(a,b):
            nonlocal result
            root_a=find(a)
            root_b=find(b)
            print(a,b,"  ",root_a,root_b)
            if root_a==root_b:
                return False
            
            parent[root_b]=root_a#wrote parent[b]=a 
            result-=1


            return True
        

        for dad in range(len(isConnected)):
            #dad + 1,
            for child in range(len(isConnected)):
                if isConnected[dad][child] ==0:
                    continue
                union(dad,child)
        return result
Penter=Solution()
a=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(Penter.findCircleNum(a))