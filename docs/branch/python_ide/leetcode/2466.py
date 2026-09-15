class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        #dp[n]=sum(dp[n-i])

        dp=[1]

        for rs in range(1,high+1):
            child=[]
            for far in [zero,one]:
                if rs-far>=0:
                    child.append(dp[rs-far])
            dp.append(sum(child))
        result=0
        for rs in range(low,high+1):
            result+=dp[rs]
        return result%(10**9+7)
penter=Solution()
low=200;high=200;zero=10;one=1
print(penter.countGoodStrings(low,high,zero,one))