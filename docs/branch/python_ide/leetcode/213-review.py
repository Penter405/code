class Solution:
    def rob(self, nums: list[int]) -> int:
        def get(begin,end):
            dp=[]

            def cheak(data):
                if len(data)==0:
                    return 0
                return max(data)

            for money in nums[begin:end]:
                dp.append(  max(money+cheak(dp[:-1]),cheak(dp)))
            dp.append(0)
            return max(dp)
        return max(get(0,len(nums)-1) ,  get(1,len(nums)), nums[0])


penter=Solution()
nums=[2,3,2]
print(penter.rob(nums))