import time
from collections import defaultdict
start = time.time()
middle=time.time()
middle2=time.time()
middle3=time.time()
middle4=time.time()
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        global middle,middle2,middle3,middle4
        result=-1
        dp=defaultdict(list)
        frees={}
        #tree one build
        def get_free(index:int,big_factor):
            nonlocal frees
            if index in frees:
                return frees[index]
            result=0
            lindex=-1
            for factor,price in items:
                #price==free
                lindex+=1
                if lindex==index:
                    continue
                if factor%big_factor==0:#this row was this-> if big_factor%factor==0:
                    result+=1
            frees[index]=result
            return result
        index=-1




        #we can make this without a set to cheak whether repeating
        for guy_f, guy_p in items:
            index+=1
            for costed_money in sorted(list(dp.keys()).copy(),reverse=True):
                for item_got in dp[costed_money]:
                    if costed_money+guy_p>budget:
                        continue

                    dp[costed_money+guy_p].append(item_got+1+get_free(index,guy_f))
            if guy_p>budget:
                continue
            dp[guy_p].append(1+get_free(index,guy_f))
        middle=time.time()


        got_free=[]
        for all_in_this_cost in range(budget+1):
            if all_in_this_cost not in dp:
                got_free.append(0)
            else:
                got_free.append(max(dp[all_in_this_cost]))
        result=max(result,max(got_free+[0]))
        dp.clear()
        middle2=time.time()
        dp2=[0 for _ in range(budget+1)]#for this we only save got, dont save took because no more free

        for guy_f, guy_p in items:
            if guy_p<=budget:
                dp2[guy_p]=1
        result=max(result,max(dp2+[0]))

        #and we need to cheak every in dp2 initialized , because they are noded of tree2
        middle3=time.time()
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
        middle4=time.time()

        for cosing in range(len(got_free)):
            #print(cosing)
            for legal_dp1_cost in range(0,budget-(cosing)+1):
                #print(cosing+legal_dp1_cost,cosing,legal_dp1_cost)
                result=(max(result,got_free[legal_dp1_cost]+dp2[cosing]))
        return result

items =[[579,35],[635,21],[432,73],[1441,34],[1211,24],[1075,79],[1165,7],[1340,13],[182,57],[838,20],[801,29],[221,57],[1202,77],[821,34],[579,81],[619,6],[982,15],[802,20],[280,6],[242,68],[332,51],[870,8],[497,17],[1041,37],[82,61],[804,46],[874,1],[1403,8],[665,20],[771,61],[1390,4],[1072,9],[1149,32],[1024,25],[1248,25],[1055,67],[748,28],[415,7],[199,81],[1160,83],[1217,36],[760,51],[1046,77],[592,29],[1401,60],[830,81],[1352,1],[879,6],[731,21],[992,78],[1056,18],[1094,81],[86,53],[96,58],[404,10],[1479,29],[663,67],[639,29],[1455,76],[687,15],[359,23],[737,57],[477,53],[645,66],[1415,60],[684,31],[916,35],[647,48],[143,13],[1288,48],[408,70],[109,23],[914,28]]
budget = 83
print(Solution.maximumSaleItems(None,items,budget))
end = time.time()
print("all",f"{end-start:.10f}")
print("first dp",f"{middle-start:.10f}")
print("cheak dp table",f"{middle2-middle:.10f}")
print("init second dp",f"{middle3-middle2:.10f}")
print("second dp",f"{middle4-middle4:.10f}")
print("get answer by two dp",f"{end-middle4:.10f}")
"""
83
all 0.5909194946
first dp 0.5759844780
cheak dp table 0.0142560005
init second dp 0.0000171661
second dp 0.0000000000
get answer by two dp 0.0003368855
"""