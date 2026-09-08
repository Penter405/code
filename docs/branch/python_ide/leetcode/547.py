class union_find:
    def __init__(self, n):
        parent=range(n)
        rank=[1 for _ in range(n)]
    @static_method
    def get_root(self,me):
        if parent[me]==me:
            return me
        return get_root(parent[me])
    
    def try_union(self, a,b):
        root_a=get_root(a)
        root_b=get_root(b)
        if root_a==root_b:
            return False
        if rank[a]>=rank[b]:
            parent[b]=a
            rank[a]+=rank[b]
            rank[b]=0
            
        else:
            parent[a]=b
            rank[b]+=rank[a]
            rank[a]=0

        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ob=union_find(len(isConnected))
        for dad in range(len(isConnected)):
            for child in range(len(isConnected)):
                ob.try_union(dad, child)
                #fail to marge
                #they are in same grupe already
                    
                #they can be marge


        return len(isConnected)-ob.rank.count(0)
