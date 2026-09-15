class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        #only data is cost vector (0) 1-2-3-n-out
        
        def cost(n):
            return costs[n-1]
                
        dp=[0]
        for rs in range(1,n+1):
            child=[]
            for i in range(1,4):
                if rs-i>=0:
                    child.append(i**2+dp[rs-i])
            dp.append(cost(rs)+min(child))
        return dp[-1]


penter=Solution()
n=3
costs=[9,8,3]
print(penter.climbStairs(n,costs))