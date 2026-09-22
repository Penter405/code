class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        if total%2!=0
            at most separate to x, x+1  
            we see far from x and then +1
        """
        part=sum(stones)
        is_135=part%2!=0
        part//=2

        dp=[0]*part+[1]

        for guy in stones:
            
            for place in range(len(dp)):
                if not(0<=place+guy<=len(dp)-1):
                    continue
                if dp[place+guy]==1:
                    dp[place]=1
        
        result=0
        if is_135:
            result+=1
        
        for rs in dp:
            if rs==1:
                return result
            result+=2
        return result

stones=[31,26,33,21,40]
print(Solution.lastStoneWeightII(None,stones))