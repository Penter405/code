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
            if guy_p>budget:
                continue
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

        #and we need to cheak every in dp2 initialized , because they are noded of tree2
        for cosing in range(len(got_free)):
            #print(cosing)
            for legal_dp1_cost in range(0,budget-(cosing)+1):
                #print(cosing+legal_dp1_cost,cosing,legal_dp1_cost)
                result=(max(result,got_free[legal_dp1_cost]+dp2[cosing]))




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
                for legal_dp1_cost in range(0,budget-(costed_money+guy_p)+1):
                    result=(max(result,got_free[legal_dp1_cost]+dp2[costed_money]+1))
                #if we never run that for loop
                result=max(result,dp2[costed_money]+1)



        return result

items = [[1421,11],[257,25],[685,57],[1129,51],[121,73],[415,72],[195,57],[908,62],[1451,15],[230,8],[399,66],[523,22],[987,76],[663,38],[18,19],[160,37],[169,48],[742,14],[397,66],[1336,2],[362,26],[1241,36],[43,21],[1322,52],[345,27],[1076,70],[1399,13],[437,54],[943,89],[503,25],[1385,74],[640,32],[1250,47],[1175,79],[1038,34],[41,40],[884,7],[1461,10],[746,75],[406,66],[1202,40],[164,22],[498,51],[703,35],[944,30],[192,57],[983,89],[1234,33],[1072,27],[889,77],[370,80],[835,64],[1030,66],[1275,29],[853,19],[1061,15],[1437,13],[1198,54],[846,71],[806,65],[1246,90],[638,25],[1374,5],[1161,57],[1041,61],[800,74],[816,16],[133,27],[1145,89],[913,62],[176,6],[1017,42],[951,24],[586,8],[1271,40],[891,89],[1061,66],[1466,62],[1398,14],[646,68],[1279,34],[1095,5],[1348,55],[411,22],[183,78],[176,43],[540,43],[1285,36],[1037,9],[502,64],[1365,54],[988,91],[860,6],[1169,89],[1320,9],[719,84],[1393,34],[110,46]]
budget = 91
print(Solution.maximumSaleItems(None,items,budget))