class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        result=-1
        dp=[list() for _ in range(budget+1)]

        i_can_get_free=dict()
        #tree one build
        def get_free(index:int,big_factor):
            result=0
            lindex=-1
            for factor,price in items:
                #price==free
                lindex+=1
                if lindex==index:
                    continue
                if factor%big_factor==0:#this row was this-> if big_factor%factor==0:
                    result+=1
            return result
        index=-1
        for guy_f, guy_p in items:
            index+=1
            for costed_money in range(len(dp)):
                for item_got,members_we_have_took in dp[costed_money]:
                    if costed_money+guy_p>budget:
                        continue
                    if index in members_we_have_took:
                        continue
                    member2=members_we_have_took.copy()
                    member2.add(index)
                    dp[costed_money+guy_p].append((item_got+1+get_free(index,guy_f),member2))
            dp[guy_p].append((1+get_free(index,guy_f),set([index])))

        got_free=[]
        for all_in_this_cost in dp:
            if len(all_in_this_cost)==0:
                got_free.append(0)
            else:
                got_free.append(max(all_in_this_cost)[0])
        result=max(result,max(got_free+[0]))
        
        dp2=[0 for _ in range(budget+1)]#for this we only save got, dont save took because no more free

        for guy_f, guy_p in items:
            if guy_p<=budget:
                dp2[guy_p]=1
        result=max(result,max(dp2+[0]))
        for costed_money in range(len(dp2)):
            if dp2[costed_money]==0:
                continue
            for guy_f, guy_p in items:
                if costed_money+guy_p>budget:
                    continue
                if dp2[costed_money]+1<dp2[costed_money+guy_p]:
                    continue
                dp2[costed_money+guy_p]=dp2[costed_money]+1
                #search dp table here cheak if legal
                #can we greedy?
                """
                sort dp table?
                we should only get these cost both sum at most to budget and from each dp cost get maximum
                """
                for legal_dp1_cost in range(0,budget-(costed_money+guy_p)):
                    result=(max(result,got_free[legal_dp1_cost]+dp2[costed_money]+1))
                #if we never run that for loop
                result=max(result,dp2[costed_money]+1)



        return result

items = [[2,4],[3,2],[4,1],[6,4],[12,4]]
budget = 8  #expect 10
print(Solution.maximumSaleItems(None,items,budget))