class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        #move to right of nums list
        #ever visit=score
        #each time 135 to or back to 246, lose x score
        at135=[0]*len(nums)
        at246=[0]*len(nums)
        if nums[0]%2==0:
            at246[0]=nums[0]
            at135[0]=float("-inf")
        else:
            at135[0]=nums[0]
            at246[0]=float("-inf")


        for index in range(1,len(nums)):
            if nums[index]%2==0:
                at246[index]=nums[index]+max(at246[index-1],at135[index-1]-x)
                at135[index]=at135[index-1]
            else:
                at135[index]=nums[index]+max(at135[index-1],at246[index-1]-x)
                at246[index]=at246[index-1]
        return max(max(at135),max(at246))
nums = [2,4,6,8]
x = 3

Solution.maxScore(None,nums,x)