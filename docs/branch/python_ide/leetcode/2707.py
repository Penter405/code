class Solution:
    #@staticmethod
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        """
        split include me[index]=   best cutted that non-overlapping(dont take same index twice)
        for s ( because we cheak by the string s first, the premax table always saves currect largest in index, premax works well)  
            buffer;front index;back index
            for guy (but only see front can uses premax)

            if not match: continue

            #now match
            split[back index]=max(self, sizeof the str+ get(front index-1))

        """
        def get(index):
            if index<0:
                return 0
            return split[index]
        split=[0]*len(s)
        for back in range(len(s)):
            #max_now=0
            for word in dictionary:

                front=back
                match=True
                for char in word[::-1]:
                    if front<0:
                        match=False
                        break
                    if char==s[front]:
                        front-=1
                    else:
                        match=False
                        break
                
                if not match:
                    continue
                front+=1
                #now match
                split[back]=max(split[back],len(word)+max(split[:front]+[0]))
                #max_now=max(max_now,split[back])

            #for rs in range(back):
            #    split[rs]=max(split[rs],max_now)
        return len(s)-max(split)
s = "ecolloycollotkvzqpdaumuqgs"
print(len(s))
dictionary = ["flbri","uaaz","numy","laper","ioqyt","tkvz","ndjb","gmg","gdpbo","x","collo","vuh","qhozp","iwk","paqgn","m","mhx","jgren","qqshd","qr","qpdau","oeeuq","c","qkot","uxqvx","lhgid","vchsk","drqx","keaua","yaru","mla","shz","lby","vdxlv","xyai","lxtgl","inz","brhi","iukt","f","lbjou","vb","sz","ilkra","izwk","muqgs","gom","je"]
print(Solution.minExtraChar(None,s,dictionary))