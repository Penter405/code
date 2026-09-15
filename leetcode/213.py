class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[nums[0]]
        rob1=[True]

        for rs in range(1,len(nums)):
            child=0
            did_1=False
            for index in range(len(dp)-1):
                if dp[index]>child:
                    if rs ==len(nums)-1 and rob1[index]:
                        continue
                    did_1=rob1[index]
                    child=dp[index]
            dp.append(child+nums[rs])
            rob1.append(did_1)
        

        return max(dp)



penter=Solution()
nums=[1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]#41
print(penter.rob(nums))