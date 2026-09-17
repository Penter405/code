class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        """
        intenger can be nagative
        if sum(arr)>0 : we can see it as a cycle
        if sum(arr)<0 :just dp to the arr, dont times k
        """
        bot=sum(arr)
        if bot<0 or k==1:
            best=0
            dp=None
            for rs in arr:
                if dp==None:
                    dp=rs
                    best=max(0,rs)
                    continue
                dp=(max( rs , rs+dp ))
                best=max(best,dp)
            return dp%(10**9+7)
        else:
            #cheak its cycle with arr*2, and get the sub array's begin and end, using some math after we got it
            best=0
            dp=None
            begin=None
            end=None
            for rs in arr*2:
                if dp==None:
                    dp=rs
                    best=max(0,rs)
                    continue
                dp=(max( rs , rs+dp ))
                best=max(best,dp)
            return dp%(10**9+7)


            if k==2:
                return best
            