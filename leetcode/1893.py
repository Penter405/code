class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        include=[0]*52
        for start,end in ranges:
            include[start]+=1
            include[end+1]-=1
        now=0
        for index,element in enumerate(include):
            now+=element
            if left<=index<=right and now<=0:
                return False

        return True
