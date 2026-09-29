from collections import deque,defaultdict
import heapq
class Solution:
    @staticmethod
    def minCut(self, s: str) -> int:
        """
        can we do two pointer on palindrome, probably no
        """

        """
        data="wassddfddud"
        """

        """
        to me max= max( just pick me + all that me in pal with less child sum)
        i pick = child max might lose 2 , but i take one, one left, so we need to try all


        solution : 
        get all sub pal o(2*n*n)
        for loop s: o(n)
            me=(i am single(1)+ my index-1 value) || (value of i am in pal+pal min index-1)# require a dict table that key:p2, value:p1 o(n)


        total-> o(n**2)

        """
        def get(n):
            if n<0 or n>len(s)-1:
                return 0
            return palmin[n]


        #get all sub pal
        point_back=[[rs] for rs in range(len(s))]
        for rs in range(len(s)):
            point_back[rs]=[rs]
        for rs in range(len(s)):
            pe=rs
            p1=pe
            p2=pe
            while True:
                if p1-1<0 or p2+1>len(s)-1:
                    break
                if s[p1-1]!=s[p2+1]:
                    break
                p1-=1;p2+=1
                point_back[p2].append(p1)
        for rs in range(len(s)-1):
            pe1=p1=rs
            pe2=p2=rs+1
            if s[pe1]!=s[pe2]:
                continue
            point_back[pe2].append(pe1)
            while True:
                if p1-1<0 or p2+1>len(s)-1:
                    break
                if s[p1-1]!=s[p2+1]:
                    break
                p1-=1;p2+=1
                point_back[p2].append(p1)
                



        #get result
        #me sub=before+1
        palmin=[0]*len(s)
        for rs in range(len(s)):
            min_child_took=None
            for friend in point_back[rs]:
                if min_child_took==None:
                    min_child_took=get(friend-1)
                min_child_took=min(min_child_took,get(friend-1))
            if min_child_took==None:
                min_child_took=0


            #get result here
            palmin[rs]=1+min_child_took
        

        return palmin[-1]-1
s="efe"
print(Solution.minCut(None,s))