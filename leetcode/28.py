class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        rs=len(haystack)-len(needle)+1
        for i in range(rs):
            print(haystack[i:i+len(needle)],needle)
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1