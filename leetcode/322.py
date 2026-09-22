class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        weighted BFS (aka dikjsta)
        """
        coins.sort(reverse=True)
        if amount==0:
            return 0
        dp=[-1]*(amount+1)
        dp[-1]=0
        for rs in coins:
            if not(rs<=amount):
                continue
            dp[-rs-1]=1
        
        while True:
            if dp[0]!=-1:
                return dp[0]
            is_updating=False
            for place in range(len(dp)-1, -1 ,-1):
                for guy in coins:
                    if not(0<=place+guy<=len(dp)-1 and dp[place+guy]!=-1):
                        continue
                    if dp[place]==-1 or dp[place+guy]+1<dp[place]:
                        is_updating=True
                        dp[place]=dp[place+guy]+1
            if not(is_updating):
                return -1

coins = [2,4,6,8,10,12,14,16,18,20,22,24]
amount = 9999
print(Solution.coinChange(None,coins,amount))