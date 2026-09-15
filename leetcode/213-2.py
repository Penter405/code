class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def get(begin,end):
            def find(n):
                if len(dp)<n:
                    return 0
                return dp[n]
            dp=[]
            for rs in range(begin,end):
                if rs==begin:
                    dp.append(nums[rs])
                    continue
                child=0
                for index in range(len(dp)-1):
                    if dp[index]>child:
                        child=dp[index]
                dp.append(max(dp[-1], child+nums[rs]))
            #print(len(dp),dp)
            if len(dp)==0:
                return 0
            return max(dp)
        return max( get(1,len(nums))  , get(0,len(nums)-1), nums[0])



penter=Solution()
nums=[1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]#41
print(penter.rob(nums))