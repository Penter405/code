from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        """init"""
        pointed=defaultdict(int)
        point=defaultdict(list)
        result=[]
        def dfs(me):
            if pointed[me]!=0:
                return 0
            pointed[me]=-1
            #now me is 0 pointed
            result.append(me)
            for child in point[me]:
                pointed[child]-=1
            for child in point[me]:
                dfs(child)
        #create graph like dict
        #must -> okay
        for okay,must in prerequisites:
            pointed[okay]+=1
            point[must].append(okay)

        """main"""
        for guy in range(numCourses):
            if pointed[guy]==0:
                #print(guy)
                dfs(guy)
        #print(result)
        return len(result)==numCourses
Penter=Solution()
a=2
b=[[1,0]]
print(Penter.canFinish(a,b))