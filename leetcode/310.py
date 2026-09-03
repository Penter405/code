#attemped, tree solution
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #0 based
        point=defaultdict(list)
        for a,b in edges:
            point[a].append(b)
            point[b].append(a)
        
        result=0
        #postorder
        def dfs(me):
            nonlocal result, went
            if me in went:
                return 0

            max_child=0
            for child in point[me]:
                max_child=max(max_child,dfs(child))
            if max

            return max_child+1

        for rs in range(n):
            went=set()
            result=max(result,dfs(rs))