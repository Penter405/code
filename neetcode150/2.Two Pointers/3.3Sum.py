#one version in leetcode :leetcode/15.py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hash={-(nums[0]+nums[1]):[[nums[0],nums[1]]]}
        #print(nums)
        #print(hash)
        #print("origin")
        hash2={}
        result=[]
        for first in range(2,len(nums)):
            #end dont include
            #print(first)
            #print(hash)
            if nums[first] in hash:
                #print(f"{nums[first]} in hash")
                for bot in hash[nums[first]]:
                    #print(f"guy is {nums[first]} and {bot}")
                    guy=tuple(bot+[nums[first]])
                    #print(guy)
                    if guy not in hash2:
                        #print(f"{guy} is unique")
                        hash2[guy]=1
                        result.append(list(guy))
            #no matter in hashtable, add 
            for second in range(0,first):
                if -(nums[second]+nums[first]) in hash:
                    hash[-(nums[second]+nums[first])].append([nums[second],nums[first]])
                else:
                    hash[-(nums[second]+nums[first])]=[[nums[second],nums[first]]]
                
        return result

