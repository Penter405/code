class Solution:
    @staticmethod
    def lastStoneWeightII(stones: list[int]) -> int:
        #store new= (store a-b), if 0 -> no store
        want=sum(stones)//2
        dp=[1]+[0]*(want)
        for guy in stones:
            t=list()
            for place in range(len(dp)):
                if dp[place]==0:
                    continue
                if place+guy> len(dp)-1:
                    continue
                t.append(place+guy)
            if guy> len(dp)-1:
                continue
            dp[guy]=1
            for rs in t:
                dp[rs]=1
        for rs in range(len(dp)-1,-1,-1):
            if dp[rs]==1:
                return sum(stones)-rs*2
stones = [31,26,33,21,40]
print(Solution.lastStoneWeightII(stones))
