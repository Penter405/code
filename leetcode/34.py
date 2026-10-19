class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left=0
        right=len(nums)-1
        result=[]

        while True:
            if right<left:
                result.append(-1)
                break
            if left==right:
                if nums[left]!=target:
                    result.append(-1)
                else:
                    result.append(left)
                break

            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1

            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid
        
        left=0
        right=len(nums)-1
        while True:
            if right<left:
                result.append(-1)
                break
            if left==right:
                if nums[left]!=target:
                    result.append(-1)
                else:
                    result.append(left)
                break

            mid=(left+right)//2+1
            if nums[mid]>target:
                right=mid-1

            elif nums[mid]<target:
                left=mid+1
            else:
                left=mid
        return result