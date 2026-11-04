class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        s=bin(abs(n))[2:]
        now=x
        ever=False
        for rs in s[::-1]:
            if ever:
                now*=now
            ever=True
            if rs=="1":
                res*=now

        if n>=0:
            return res
        return 1/res

Solution.myPow(None,2.00,2**31-1)