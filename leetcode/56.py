class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=list()
        for i in range(0,len(intervals)):
            if len(result)==0:
                result.append(intervals[i])
                continue
            if result[-1][0]<=intervals[i][0] and intervals[i][0]<=result[-1][1]:
                result[-1][1]=max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])
        return result