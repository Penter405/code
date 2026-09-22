from collections import defaultdict
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        dp=[picked][now 1 and 0]
        """
        #1 , 0
        def get(member):
            return (member.count("1"),member.count("0"))
        dp=defaultdict(set)
        index=-1
        for guy in strs:
            index+=1
            a=get(guy)
            for rs in range(len(dp)-1,-1,-1):
                for element in dp[rs]:
                    if a[0]+element[0]<=n and a[1]+element[1]<=m:
                        dp[rs+1].add((a[0]+element[0],a[1]+element[1]))
            if a[0]<=n and a[1]<=m:
                dp[0].add(a)
            

        return max(list(dp.keys())+[-1])+1
strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
m = 9
n = 80
print(Solution.findMaxForm(None,strs,m,n))
