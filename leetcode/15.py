#one version in neetcode :neetcode150/2.Two Pointers/3.3Sum.py
class Solution:
    def rm_useless(self,s):
        result=[s[0]]
        if len(s)==0:
            return []
        ed=s[0]
        did=0
        for rs in range(1,len(s)):
            if s[rs]==ed:
                did+=1
            else:
                did=0
                ed=s[rs]
            if did<3:
                result.append(s[rs])
            
        return result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums=self.rm_useless(nums)
        hash={}
        #print(nums)
        #print(hash)
        #print("origin")
        hash2={}
        result=[]
        for first in range(1,len(nums)-1):
            #end dont include
            #print(first)
            #print(hash)
            left=0
            right=len(nums)-1
            while left<right:
                #print(left,first,right)
                if right==first:
                    #print(f"right same")
                    right-=1
                    continue
                if left==first:
                    #print("left same")
                    left+=1
                    continue
                if nums[left]+nums[right]>(-(nums[first])):
                    #print(f"{nums[left]+nums[right]} bigger than {-(nums[first])}")
                    right-=1
                elif nums[left]+nums[right]<(-(nums[first])):
                    #print(f"{nums[left]+nums[right]} smaller than {-(nums[first])}")
                    left+=1
                elif nums[left]+nums[right]==(-(nums[first])):
                    #print(f"{nums[left]+nums[right]} same {-(nums[first])}")
                    bot=[nums[left],nums[right],nums[first]]
                    bot.sort()
                    if tuple(bot) not in hash:
                        result.append(bot)
                        hash[tuple(bot)]=1
                    right-=1
        return result
