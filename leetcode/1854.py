class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        #input 1950  -> -1950  -> 0
        #input 2050 -> -1950  -> 100
        #-> 101 and [)  -> 101
        include=[0]*101
        for start,end in logs:
            start-=1950
            end-=1950
            include[start]+=1
            include[end]-=1
        result=1950
        rnow=0
        now=0
        for index,value in enumerate(include):
            year=index+1950
            now+=value
            if now>rnow:
                result=year
                rnow=now

        
        return result