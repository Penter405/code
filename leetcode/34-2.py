class Solution:
    @staticmethod
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def get(find_left):
            left=0
            right=len(nums)-1
            if len(nums)==0:
                return -1
            while left<=right:
                if find_left:
                    mid=(left+right)//2
                else:
                    mid=(left+right)//2+1
                if left==right:
                    if nums[left]!=target:
                        return -1
                    return left
                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                elif nums[mid]==target:
                    if find_left:
                        #[...7 7 7 7..]
                        #        /
                        right=mid
                    else:
                        left=mid
            return -1
        return [get(True),get(False)]

nums =[2,2]
target=8
print(Solution.searchRange(None,nums,target))