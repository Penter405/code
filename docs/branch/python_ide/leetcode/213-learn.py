class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def get(begin, end):
            now=last=best=0
            for money in nums[begin:end]:
                now=max(best, money+last )
                last=best
                best=now
            return best
        
        return max(get(0,-1), get(1,len(nums)),nums[0])