"""
change now, change later
change perviously
2 by 2 square
if we can make sure left sides match right side, 
"""
class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        dp=[]#can we use less status than recursion?
        result=0
        l1=float("-inf")
        l2=float("-inf")
        for index in range(len(nums1)):
            if l1>=nums1[index] or l2>=nums2[index]:
                print(index)
                nums1[index],nums2[index]=nums2[index],nums1[index]
                result+=1


            l1=nums1[index]
            l2=nums2[index]
        return result


nums1 = [0,4,4,5,9]
nums2 = [0,1,6,8,10]
Solution.minSwap(None,nums1,nums2)