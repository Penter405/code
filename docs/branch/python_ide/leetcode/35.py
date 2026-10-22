class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<right:
            
            mid=(left+right+1)//2
            if nums[mid]>target:
                right=mid-1
            else:
                left=mid
        if nums[left]==target:
            return left
        elif target<nums[left]:
            return left
        return left+1