#did not finish
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #0 based, totoal len =numCourses
        #after:before =tes
        #before -> after
        #also have to cheak if it diracted

        """1 init"""
        pointed=defaultdict(int)
        point=defaultdict(list)
        p=[]
        for after,before in prerequisites:
            point[before].append(after)
            pointed[after]+=1
        #for after in pointed.keys():
        #    p.append([  len(pointed[after]) , after  ])
        #p.sort()#default small to big
        result=[]

        """2 main"""
        while len(result)!=numCourses:
            
            target=[]
            """cheak zero"""
            for guy in pointed.keys():
                if (pointed[guy])==0:
                    target.append(guy)
            result.extend(sorted(target))
            """remove line"""
            for guy in target:
                for ob in point[guy]:
                    pointed[ob]-=1
        return len(result)==numCourses

                    