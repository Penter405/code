class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        result=0
        cost.sort(reverse=True)
        bought=0
        for rs in cost:
            if bought==2:
                bought=0
                continue
            result+=rs
            bought+=1
        return result