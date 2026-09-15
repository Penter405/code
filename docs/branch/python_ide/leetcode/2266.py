class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        result=1
        dp=[1,1,2,4]
        dp79=[1,1,2,4,8]
        def get(n):
            if len(dp)<n+1:
                while len(dp)<n+1:
                    dp.append(dp[-1]+dp[-2]+dp[-3])
            return dp[n]
        def get79(n):
            if len(dp79)<n+1:
                while len(dp79)<n+1:
                    dp79.append(dp79[-1]+dp79[-2]+dp79[-3]+dp79[-4])
            return dp79[n]
        def part(guys:list):
            last=None
            result=[]
            for guy in guys:
                if last==None or guy!=last:
                    result.append([])
                result[-1].append(guy)
                last=guy
            return result

        
        for team in part(pressedKeys):
            if "7" ==team[0] or "9" ==team[0]:
                result*=get79(len(team))
            else:
                result*=get(len(team))
        return result%(10**9+7)


penter=Solution()
pressedKeys="444479999555588866"
print(penter.countTexts(pressedKeys))
    