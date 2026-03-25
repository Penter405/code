class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p2=0
        meet=-1
        now=0
        while p2<len(haystack):
            print(p2,now)
            
            if haystack[p2]==needle[now]:
                if 
                if now>=len(needle)-1 and meet!=-1:
                    print(p2,now)
                    return meet
                if now==0:
                    meet=p2
                now+=1
                p2+=1

                
            else:
                p2+=1
                now=0
                meet=-1
        if meet!=-1:
            return meet
        return -1