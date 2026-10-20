class Solution:
    def search(self, nums: list[int], target: int,get_l=True) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if not get_l:
                mid=(left+right+1)//2
            
            if nums[mid]<target:
                left=mid+1
                
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]==target:
                if get_l:
                    right=mid
                else:
                    left=mid
            
        if nums[left]!=target:
            return -1
        return left


nums = [-1,0,3,5,9,9,9,9,12]
target = 9
print(Solution.search(None,nums,target,False))