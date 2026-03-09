class Solution:
    def countPrimes(self, n: int) -> int:
        result=0
        if(n==1 or n==0):
            return 0
        is_prime=[1]*n
        """for rs in is_prime:
            print(rs,end='')
        print('')
        """
        is_prime[0]=0
        is_prime[1]=0
        for i in range(n):
            if(is_prime[i]==1):
                result+=1
                for pe in range(i*2,n,i):
                    is_prime[pe]=0
            
        return result

