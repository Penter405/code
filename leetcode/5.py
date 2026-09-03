class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        for rs in range(len(s)+1):
            for pe in range(rs):
                #print(s[pe:rs])
                if s[pe:rs][::-1]==s[pe:rs]:
                    if len(s[pe:rs])>len(result):
                        result=s[pe:rs]
        return result
"""
penter=Solution()
print(penter.longestPalindrome("abba"*250))
"""