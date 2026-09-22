#attempted

"""
did i understand problem?
factor_j % factor_i == 0

注意方向！

"""

"""
new DP
dp=[set() for _ in range(budget+1)]
dp[i]=in each costed cheak members_we_have_took and number_of_got_item
"""
from collections import defaultdict
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        #if buying this item and never bought, get frees(if factor main % factor might free item==0)
        """
        dp=[number_of_got_item]
        dp.value=set saves (costed_money,members_we_have_took)
        """
        dp=defaultdict(list)
        i_can_get_free=dict()
        def get_free(index:int,big_factor):
            nonlocal i_can_get_free
            if index in i_can_get_free:
                return i_can_get_free[index]
            else:
                result=0
                lindex=-1
                for factor,price in items:
                    #price==free
                    lindex+=1
                    if lindex==index:
                        continue
                    if factor%big_factor==0:#this row was this-> if big_factor%factor==0:
                        result+=1
                    

                i_can_get_free[index]=result
                return result
        index=-1
        for guy_f, guy_p in items:
            index+=1
            for number_of_got_item in list(dp.keys()).copy():
                for costed_money,members_we_have_took in dp[number_of_got_item]:
                    if costed_money+guy_p>budget:
                        continue
                    new_cost=costed_money+guy_p
                    new_got_item=number_of_got_item
                    if index not in members_we_have_took:
                        new_got_item+=get_free(index,guy_f)
                    new_took=members_we_have_took.copy()
                    new_took.add(index)
                    dp[new_got_item+1].append((new_cost,new_took))
                    times=0
                    while True:
                        #we will make one element add up many times here
                        times+=1
                        if new_cost+guy_p*times>budget:
                            break
                        dp[new_got_item+1+times].append((new_cost+guy_p*times,new_took))


            if guy_p>budget:
                break
            got_free=get_free(index,guy_f)
            dp[1+got_free].append((guy_p,set([index])))
            times=0
            while True:
                times+=1
                if guy_p*(times+1)>budget:
                    break
                dp[1+got_free+times].append((guy_p*(times+1),set([index])))
        return max(dp.keys()) if len(dp)>0 else 0
items = [[44,1],[76,23],[17,1],[83,6],[1,16]]
budget = 42
print(Solution.maximumSaleItems(None,items,budget))