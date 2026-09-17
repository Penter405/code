class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        """
        do twice take and skip OR do in the same time
        """

        dp=[]
        dpnag=[]
        
        for rs in nums:
            if len(dp)==0:
                dp.append(rs)
                dpnag.append(rs)
                continue
            
            dp.append(max(rs,rs+dp[-1]))
            dpnag.append(min(rs,rs+dpnag[-1]))
        dp.append(0)
        dpnag.append(0)
        print(dp)
        print(dpnag)
        return max(max(dp),abs(min(dpnag)))

penter=Solution()
nums=[-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]
print(sum([-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]))
print(sum(nums))
print(penter.maxAbsoluteSum(nums))