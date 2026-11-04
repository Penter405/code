class Solution:
    def myPow(self, x: float, n: int) -> float:
         power=abs(n)
         result=1.0

         while power>0:
            if power % 2==1:
                result*=x
            x*=x
            power//=2

         return 1.0 / result if n<0 else result

Solution.myPow(None,2.01,100000)