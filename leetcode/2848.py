List=list
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        include=[0]*102
        for start,end in nums:
            include[start]+=1
            include[end+1]-=1

        result=0
        now=0
        for element in include:
            now+=element
            if now>0:
                result+=1
        return result
    