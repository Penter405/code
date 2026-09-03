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

#version two
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        #print(nums)
        result=set()
        for i in range(len(nums)-2):

            p1=i+1
            p2=len(nums)-1
            while p2>p1 and p2>=0 and p1<len(nums):
                #print(i,p1,p2)
                #print(nums[i],nums[p1],nums[p2])
                if p1==p2:
                    p2-=1
                if nums[p1]+nums[p2]+nums[i]==0:
                    #print("good")
                    x=(nums[i],nums[p1],nums[p2])
                    #print(type(x))
                    result.add(x)
                    while p1<p2 and nums[p1]==nums[p2]:
                        p2-=1
                if nums[p1]+nums[p2]+nums[i]>=0:
                    p2-=1
                elif nums[p1]+nums[p2]+nums[i]<0:
                    p1+=1
                else:
                    print("error")
        return list(result)
"""
#12345
2+4=8
1+2=3
1+3=4
1+4=5

"""