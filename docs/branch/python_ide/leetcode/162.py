class Solution:
    @staticmethod
    def findPeakElement(self, nums: list[int]) -> int:
        #if x > his left and x>his right: x =result
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if (right-left)%2!=0:
                mid+=1
            if left==right:
                return left
            
            if nums[mid]>nums[mid-1]:
                left=mid
            else:
                right=mid-1

nums=[1,2,1]
print(Solution.findPeakElement(None,nums))