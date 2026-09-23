import time
from collections import defaultdict
start = time.time()
middle=time.time()
middle2=time.time()
middle3=time.time()
middle4=time.time()
find_free=time.time()
find_free2=time.time()
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        global middle,middle2,middle3,middle4,find_free,find_free2
        result=-1
        dp=defaultdict(int)
        frees=[None for _ in range(len(items))]
        #tree one build
        def get_free(index:int,big_factor):
            nonlocal frees
            if frees[index]!=None:
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
        find_free=time.time()
        for rs in range(len(items)):
            get_free(rs,items[rs][0])
        find_free2=time.time()

        #we can make this without a set to cheak whether repeating
        #this is not using dp beacue we do have a best solution for saved on dp table
        for guy_f, guy_p in items:
            index+=1
            for costed_money in sorted(list(dp.keys()).copy(),reverse=True):
                if costed_money+guy_p>budget:
                    continue

                dp[costed_money+guy_p]=max(dp[costed_money+guy_p],dp[costed_money]+1+frees[index])
            if guy_p>budget:
                continue
            dp[guy_p]=max(dp[guy_p],1+frees[index])
        middle=time.time()


        got_free=dp
        """
        for all_in_this_cost in range(budget+1):
            if all_in_this_cost not in dp:
                got_free.append(0)
            else:
                got_free.append(max(dp[all_in_this_cost]))
        """
        result=max(result,max(list(got_free.values())+[0]))
        #dp.clear()
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
        result=max(result,max(dp2+[0]))
        for cosing in got_free.keys():
            #print(cosing)
            for legal_dp1_cost in range(0,budget-(cosing)+1):
                #print(cosing+legal_dp1_cost,cosing,legal_dp1_cost)
                result=(max(result,got_free[cosing]+dp2[legal_dp1_cost]))
        return result

items =[[1073,48],[956,11],[658,38],[829,20],[47,1],[237,21],[1095,15],[1335,4],[533,19],[506,5],[252,9],[803,2],[1451,17],[629,1],[195,39],[1023,18],[654,32],[1242,23],[184,26],[423,19],[958,37],[1416,27],[39,35],[309,33],[557,17],[71,5],[1309,24],[847,6],[1442,36],[483,31],[829,9],[927,26],[51,24],[1076,15],[1296,24],[252,21],[1417,50],[1175,11],[531,21],[68,19],[1438,30],[471,30],[1139,27],[491,48],[1024,29],[1351,9],[387,14],[523,28],[1101,22],[724,31],[1211,43],[772,44],[90,24],[926,38],[239,33],[1065,42],[682,14],[870,41],[825,5],[737,40],[28,6],[1493,8],[94,7],[332,12],[482,44],[298,42],[572,14],[1073,40],[1451,38],[1067,1],[1278,30],[442,40],[118,13],[1025,28],[480,51],[1178,35],[1146,18],[143,36],[86,44],[1187,31],[1213,24],[540,30],[381,34],[580,7],[813,43],[851,35]]
budget = 52
print(Solution.maximumSaleItems(None,items,budget))
end = time.time()
print("all",f"{end-start:.10f}")
print("find free", f"{find_free2-find_free:.10f}")
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