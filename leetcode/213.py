class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[nums[0]]
        dp2=[nums[-1]]

        for rs in range(1,len(nums)-1):
            child=0

            for index in range(len(dp)-1):
                if dp[index]>child:
                    if rs ==len(nums)-1:
                        continue
                    child=dp[index]
            dp.append(child+nums[rs])
        
        nums2=nums[::-1]
        
        for rs in range(1,len(nums2)-1):
            child=0

            for index in range(len(dp2)-1):
                if dp2[index]>child:
                    if rs ==len(nums2)-1:
                        continue
                    child=dp2[index]
            dp2.append(child+nums2[rs])


        return max(max(dp),max(dp2))



penter=Solution()
nums=[1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]#41
print(penter.rob(nums))