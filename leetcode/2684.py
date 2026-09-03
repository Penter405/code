"""
we dont need dp, cause nodes never go back column, dp result will be same as ever went with legal relation ship

i missed a key point therefore i debug serveral time, i did not put stop recursion cheak in the front of recursion
, but i putted return if column in the most right return greedy in the front of recursion
"""




class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        #move if the value bigger than me
        #start in the first column
        #every row is column go right, and row has three way to go, up no moving or down
        # 0<= result< len(result[0])

        dp=dict()

        max_row=len(grid)
        max_size=len(grid[0])
        def recursion(row, column,parent=None):
            #print(row,column)
            if parent!=None and parent>=grid[row][column]:
                return 0
            
            if column ==max_size-1:
                return column
            #if column> max_size:
                #print("wrong")
            me=column
            #buffer=[]
            #buffer.append(str(me))
            
            if (row,column) in dp:
                return dp[row,column]
            for rs in [-1,0,1]:
                if 0<= row+rs <max_row:
                    me=max(me,recursion(row+rs,column+1,grid[row][column]))
                    """child=recursion(row+rs,column+1,grid[row][column])
                    if child > me:
                        #buffer.append(str(child) +">"+ str(me))
                        me=child
                    """
            #buffer.append("finally"+ str(me))
            #print(",  ".join(buffer))
            dp[(row,column)]=me
            return me
        result=0
        for rs in range(max_row):
            result=max(result,recursion(rs,0))
        #print(dp)
        return result

penter=Solution()
data=[[33,39,100,77,14,217],[277,179,36,35,222,179],[76,196,185,229,265,161],[267,137,250,257,45,163],[217,153,246,100,99,113],[119,119,212,38,201,210],[22,224,225,184,123,113],[141,122,255,170,121,219],[194,36,135,101,159,69],[28,69,15,64,260,90],[274,116,142,35,6,133],[97,82,106,10,152,283],[230,173,189,200,179,118]]
result=penter.maxMoves(data)
print(result)