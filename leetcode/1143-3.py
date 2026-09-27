import time
from collections import defaultdict
strat=time.time()
class Solution:
    @staticmethod
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=dict()#key value(key: int  )
        result=0
        point=defaultdict(list)#from 1 to 2
        back=defaultdict(list)
        s1=set(text1)
        s2=set(text2)
        both_uses=s1 & s2
        for a in range(len(text1)):
            for  b in range(len(text2)):
                if text1[a] not in both_uses or text2[b] not in both_uses:
                    continue
                if text1[a]!=text2[b]:
                    continue
                point[a].append(b)
                back[b].append(a)

        for a in sorted(list(point.keys())):
            for b in point[a]:
                my_child=0
                #find best child
                for first in dp.keys():
                    if first>=a:
                        continue
                    for second in dp[first]:
                        if second>=b:
                            continue
                        my_child=max(my_child,dp[first][second])

                #put inside
                if a not in dp:
                    dp[a]=dict()
                if b not in dp[a]:
                    dp[a][b]=my_child+1
                    result=max(result,my_child+1)
        return result

text1="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
text2="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(Solution.longestCommonSubsequence(None,text1,text2))
end=time.time()
print(f"{end-strat:.10f}")