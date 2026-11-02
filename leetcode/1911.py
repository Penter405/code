class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        added=nums.copy()
        erased=[0]*len(nums)
        erased[0]=float("-inf")
        for index in range(1,len(nums)):
            erased[index]=max(erased[index],erased[index-1],added[index-1]-nums[index])
            added[index]=max(added[index],added[index-1],nums[index]+erased[index-1])
        return max(max(erased),max(added))

nums=[5,6,7,8]
Solution.maxAlternatingSum(None,nums)
