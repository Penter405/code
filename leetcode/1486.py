class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        now=start
        res=now
        for i in range(1,n):
            res=res^(start+2*i)
            #print(start+2*i,res)

        return res