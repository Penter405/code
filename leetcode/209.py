class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1=-1
        p2=-1
        result=0
        all=0
        while p1<len(nums) and p2<len(nums):
            #print(p1,p2,len(nums))
            if all>=target:
                #print(nums[p1:p2+1])
                if result==0:
                    result=p2-p1
                else:
                    result=min(result,p2-p1)
                p1+=1
                all-=nums[p1]
            else:
                p2+=1
                if p2>=len(nums):
                    break
                all+=nums[p2]

        return result