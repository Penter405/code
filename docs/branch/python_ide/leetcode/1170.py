class Solution:
    @staticmethod
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        def f(d):
            bot=None
            amount=0
            for rs in d:
                if bot==None or rs<bot:
                    bot=rs
                    amount=1
                    continue
                if bot==rs:
                    amount+=1
            return amount
        q=[]
        w=[]
        for rs in queries:
            q.append(f(rs))
        for rs in words:
            w.append(f(rs))

        w.sort()
        def search(sub):
            #find last can include intenger
            #near right
            left=0
            right=len(w)-1

            while left<right:
                mid=(left+right+1)//2
                if w[mid]>sub:
                    right=mid-1
                else:
                    left=mid+1
            if left>len(w)-1:
                return -1
            if w[left]>sub:
                return len(w)-left-1
            return len(w)-left-1-1
        res=[]
        for rs in q:
            res.append(search(rs)+1)
        return res
queries = ["cbd"]
words = ["zaaaz"]
print(Solution.numSmallerByFrequency(None,queries,words))