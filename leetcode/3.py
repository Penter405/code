class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=iter(s)
        right=iter(s)
        if not s:
            return 0
        l_value=next(left)
        r_value=next(right)
        size=1
        hashset=set()
        hashset.add(r_value)
        result=1
        while 1:
            #print(hashset)
            #print(l_value)
            #print(r_value)
            try:
                #print(size)
                #print(f"result {result} vs size {size}")
                if size>result:
                    #print(f"{size} overrided result")
                    result=size
                r_value=next(right)
                while r_value in hashset:
                    size-=1
                    #print(f"{r_value} in {hashset}")
                    #print(f"{hashset} remove elemnet {l_value}")
                    hashset.remove(l_value)
                    l_value=next(left)
                    #print(f"new l value is {l_value}")
                hashset.add(r_value)
                size+=1    
            except StopIteration:
                return result