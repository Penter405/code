class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        legal=[True]*5000
        for guy in arr2:
            for rs in range(guy,guy+d+1):
                legal[rs]=False

            for rs in range(guy,guy-d-1,-1):
                legal[rs]=False
        
        res=0
        for rs in arr1:
            if legal[rs]:
                res+=1
        return res