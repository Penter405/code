class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #guy be truct by anyone
        #he dont trust anyone
        banned=set()
        trusted=defaultdict(list)
        for a, t in trust:
            #print(a,t)
            banned.add(a)
            trusted[t].append(a)
        for dont in range(1,n+1):
            if dont in banned:
                continue
            if len(trusted[dont])==n-1:
                return dont
        return -1