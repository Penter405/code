class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """init"""
        def dfs(me):
            if pointed[me]!=0:
                return 0
            pointed[me]=-1
            result.append(me)
            for child in point[me]:
                pointed[child]-=1
            for child in point[me]:
                dfs(child)
    


        result=[]
        pointed=defaultdict(int)
        point=defaultdict(list)
        #must-> okay
        for okay, must in prerequisites:
            pointed[okay]+=1
            point[must].append(okay)
        

        """main"""
        for guy in range(numCourses):
            if pointed[guy]==0:
                dfs(guy)
        if len(result)!=numCourses:
            return []
        return result