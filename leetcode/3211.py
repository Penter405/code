class Solution:
    def validStrings(self, n: int) -> list[str]:
        res=[]
        buffer=[None]*n
        def recursion(did=0,last1=True):
            if did==n:
                res.append("".join(buffer))
                return 0
            
            buffer[did]="1"
            recursion(did+1,True)
            if last1:
                buffer[did]="0"
                recursion(did+1,False)
        recursion()
        return res