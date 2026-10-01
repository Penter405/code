import time
start=time.time()
class Solution:
    @staticmethod
    def maxProfit(self, k: int, prices: list[int]) -> int:
        """
        vital status:
            sold or hold one or hold two
            money earned
            hoding how many money
        

        earn=[[] [] []]   earn[hoding]  -> [] means we can put earned, and holding
        """

        dp=[[0]*len(prices) for _ in range(k)]
        result=0
        
        for buy in range(len(prices)):
            if buy!=0:
                for bought in range(1,len(dp)):
                    dp[bought][buy]=max(dp[bought][buy],dp[bought][buy-1])
            for sell in range(buy+1,len(prices)):
                if prices[buy]<prices[sell]:
                    got=prices[sell]-prices[buy]
                    for bought in range(k-1,-1,-1):
                        best_child=dp[bought][buy]  #24.9957067966   ->  0.8514258862  if we skip max, which is a 0(n) function  , we can use postmax, its premax in fect
                        result=max(result,best_child+got)
                        if bought!=k-1:
                            dp[bought+1][sell]=max(dp[bought+1][sell],best_child+got)
            
        return result


k = 2
prices = [2,4,1]
print(Solution.maxProfit(None,k,prices))
end=time.time()
print(f"{end-start:.10f}")