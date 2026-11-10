"""
normal for loop with two pointer is o(n**2)
but now it is 
for 
for
   for
      for 
         for
   for
      for
         for
o(n**4)
for these need write down every solution rather than their amount, dp will not be faster
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        naga_max=0
        posi_max=0
        for rs in nums:
            if rs>0:
                posi_max+=rs
            else:
                naga_max+=-rs
        dp=[[set() for _ in range(3)] for _ in range(posi_max+naga_max+1)]
        #want indecx 0 value ==3 or up

        for element in nums:
            if element>=0:
                for index in range(posi_max,-naga_max-1,-1):
                    if dp[index]!=0 and -naga_max<=index+element<=posi_max:
                        for had in range(1,-1,-1):
                            for past in dp[index][had]:
                                dp[index+element][had+1].add(tuple(sorted(list(past)+[element])))
            else:
                for index in range(-naga_max,posi_max+1):
                    if dp[index]!=0 and posi_max>=index+element>=-naga_max:
                        for had in range(1,-1,-1):
                            for past in dp[index][had]:
                                dp[index+element][had+1].add(tuple(sorted(list(past)+[element])))
            dp[element][0].add((element,))
        return list(map(list,list(dp[0][2])))
nums=[-1,0,1,0]
print(Solution.threeSum(None,nums))