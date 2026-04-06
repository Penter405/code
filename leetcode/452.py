class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #marge them and count leng
        points.sort()
        count=0
        target=[]
        for i in range(len(points)):
            #print(points)
            #print(target)
            #print(i)
            if(len(target)==0):
                target.append(points[i][0])
                target.append(points[i][1])
                count+=1
            elif((points[i][0]<=target[1] and target[0]<=points[i][1])):
                target[0]=max(points[i][0],target[0])
                target[1]=min(points[i][1],target[1])
            else:
                #target die
                #we become new target, and counts more 1
                target[0]=points[i][0]
                target[1]=points[i][1]
                count+=1
        return count