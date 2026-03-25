class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result=""
        hash=dict()
        all=len(t)
        for rs in t:
            hash[rs]=0
        pointer1=0
        pointer2=-1
        while pointer1<len(s)-1:
            if pointer1>=pointer2:
                pointer2+=1
                if s[pointer2] in hash:
                    if hash[s[pointer2]]:
                        