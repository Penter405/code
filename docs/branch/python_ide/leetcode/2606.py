class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        """
        char=score
        if char in chars:
            pick it up=lose score in same index with vals

        dp= take me , or take me+ previous
        """

        bad={}
        for rs in range(len(chars)):
            bad[chars[rs]]=vals[rs]
        
        dp=[]
        def get(letter):
            if letter in bad:
                return bad[letter]
            return ord(letter)-ord('a')+1
        for rs in s:
            bot=get(rs)
            if len(dp)==0:
                dp.append(bot)
                continue
            bot=get(rs)
            dp.append( max(bot, bot+dp[-1]  )  )
        return max(*dp,0)