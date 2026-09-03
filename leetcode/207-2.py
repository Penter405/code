#solved
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        #0 based, totoal len =numCourses
        #after:before =tes
        #before -> after
        #also have to cheak if it diracted

        """1 init"""
        pointed=dict()
        point=defaultdict(list)
        p=[]
        for rs in range(numCourses):
            pointed[rs]=0
        for after,before in prerequisites:
            point[before].append(after)
            pointed[after]+=1
        #for after in pointed.keys():
        #    p.append([  len(pointed[after]) , after  ])
        #p.sort()#default small to big
        result=[]

        """2 main"""
        while len(pointed)!=0:
            target=[]
            """cheak zero"""
            for guy in pointed.keys():
                if (pointed[guy])==0:
                    target.append(guy)
            result.extend(sorted(target))
            if len(target)==0:
                return False
            """remove line"""
            for guy in target:
                for ob in point[guy]:
                    pointed[ob]-=1
                print(pointed)
                pointed.pop(guy)
                print(pointed)
        return len(result)==numCourses
Penter=Solution()
a=2
b=[[1,0],[0,1]]
print(Penter.canFinish(a,b))
print("done")
