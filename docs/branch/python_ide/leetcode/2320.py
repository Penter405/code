class Solution:
    def countHousePlacements(self, n: int) -> int:
        """
        street=2 side
        each side has n plots(1-indexed)
        

        """

        def get(n):#now possible=choose me and biggest not close + biggest not me
            now=0
            best=1#ways if dont choose me
            last=1#ways if choose me
            for _ in range(n):
                now=last+best
                last=best
                best=now
            return now
        return (get(n)**2)%(10**9+7)

penter=Solution()
n=3
print(penter.countHousePlacements(n))