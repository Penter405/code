class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            intervals.append(newInterval)
            return intervals
        if newInterval[1]<intervals[0][0]:
            intervals.insert(0,newInterval)
            return intervals
        #where=0
        ever=0
        i=-1
        #pre=0
        for _ in range(0,len(intervals)):
            i+=1
            #print(intervals)
            #print(f"seeing {i}")
            if ever==1:
                #print("ever is 1")
                if intervals[i-1][1]>=intervals[i][0]:
                    if intervals[i-1][1]<=intervals[i][1]:
                        intervals[i-1][1]=intervals[i][1]
                        #print(f"pop {i} index :{intervals[i]}")
                        intervals.pop(i)
                        i-=1
                        break
                    else:
                        intervals.pop(i)
                        i-=1
                else:
                    break
            elif (intervals[i][0]<=newInterval[1] and newInterval[0]<=intervals[i][1]):
                #print("into")
                #pre=intervals[i][0]
                ever=1
                #where=i
                intervals[i][0]=min(intervals[i][0],newInterval[0])
                if intervals[i][1]>=newInterval[1]:
                    break
                intervals[i][1]=newInterval[1]
            elif (i>0 and newInterval[0]>intervals[i-1][1] and newInterval[1]<intervals[i][0]):
                #print(i)
                intervals.insert(i,newInterval)
                ever=1
                break
        if ever==0:
            intervals.append(newInterval)
        return intervals