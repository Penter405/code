class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        s=bin(abs(n))[2:]
        now=1
        for rs in s[::-1]:
            if rs=="1":
                res*=now
            now*=x
        if n>=0:
            return res
        return 1/res

print(Solution.myPow(None,2,10))