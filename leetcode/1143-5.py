import time
strat=time.time()
class Solution:
    @staticmethod
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        premax=[[0]*len(text2) for _ in range(len(text1))]
        #dp=[0*text2 for _ in range(len(text1))]
        def get(a,b):
            if 0<=a<=len(text1)-1 and 0<=b<=len(text2)-1:
                return premax[a][b]
            return 0


        for a in range(len(text1)):
            for b in range(len(text2)):
                take_me_if_legal=0
                if text1[a]==text2[b]:
                    take_me_if_legal=1
                premax[a][b]=max(get(a-1,b-1)+take_me_if_legal,get(a-1,b),get(a,b-1))
        

        return premax[-1][-1]

text1="mhunuzqrkzsnidwbun"
#      12   3      4 56
text2="szulspmhwpazoxijwbq"
#            12   3  4 56
print(Solution.longestCommonSubsequence(None,text1,text2))
end=time.time()
print(f"{end-strat:.10f}")