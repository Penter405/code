class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p != root_q:
            if self.rank[root_p] < self.rank[root_q]:
                self.parent[root_p] = root_q
            elif self.rank[root_p] > self.rank[root_q]:
                self.parent[root_q] = root_p
            else:
                self.parent[root_q] = root_p
                self.rank[root_p] += 1
            return True

        return False


class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind(len(edges) + 1)

        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]
edges=[[1, 2], [1, 3], [2, 3]]
Penter=Solution()
Penter.findRedundantConnection()