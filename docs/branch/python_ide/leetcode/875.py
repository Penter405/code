import time
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # k -> bananas-per-hour eating speed 
        left=1
        right=max(piles)
        #find minimum-> near left
        #left must correct
        def legal(amount):
            used_h=0
            for element in piles:
                now=element//amount
                if element%amount!=0:
                    now+=1
                used_h+=now
                if used_h>h:
                    return False
            if used_h>h:
                return False
            return True
        while left<=right:
            mid=(left+right)//2
            if legal(mid):
                right=mid-1
            else:
                left=mid+1
        return left
            

piles = [312884470]
h = 312884469
st=time.time()
print(Solution.minEatingSpeed(None,piles,h))
print(time.time()-st)