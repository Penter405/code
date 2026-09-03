from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def reversed_list(x):
            new=[]
            for a,b in x:
                new.append((b,a))
            return new
        result=[]
        ever=0
        count=0
        #print(sorted(reversed_list(Counter(nums).most_common()),reverse=True))
        for time,name in sorted(reversed_list(Counter(nums).most_common()),reverse=True):
            if time!=ever:
                count+=1
            
            if count>k:
                return result
            result.append(name)
        return result

