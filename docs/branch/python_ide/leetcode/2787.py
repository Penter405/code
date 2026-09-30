class Solution:
    @staticmethod
    def numberOfWays(self, n: int, x: int) -> int:
        """
        pick up 1-n with power x
        """

        dp=[1]+[0]*(n)
        for number in range(1,n+1):
            add_me=number**x
            for rs in range(n,add_me-1,-1):
                #if rs-add_me<0:  ->  rs<add_me  ->
                #    continue
                dp[rs]+=dp[rs-add_me]
        return (dp[-1])%(10**9+7)

print(Solution.numberOfWays(None,4,1))
