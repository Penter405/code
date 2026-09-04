class Solution:
    def eventualSafeNodes(self, graph):
        #we can use list's index as key of dict
        statu=[0]*len(graph)#= -1 bad, 0 no cheaked ,1=cheaked
        good=set()
        """
        point=defaultdict(list)
        pointed=defaultdict(list)
        for i in range(len(graph)):
            point[i].extend(graph[i])
            for rs in graph[i]:
                pointed[rs].append(i)
        """

        #postorder dfs
        def dfs(me):
            if statu[me]==-1:
                return 0
            if statu[me]==1:
                if me in good:
                    return True
                else:
                    statu[me]=-1
                    return False

            statu[me]=1
            for child in graph[me]:
                if dfs(child)==False:
                    statu[me]=-1
                    return False

            
            good.add(me)
            return True
        
        for rs in range(len(graph)):
            dfs(rs)

        result=sorted(list(good))
        return result




Penter=Solution()
a=[[1,2],[2,3],[5],[0],[5],[],[]]
Penter.eventualSafeNodes(a)