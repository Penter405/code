#1:25:36 attempt
from collections import deque,defaultdict
class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        #more than 1: can cut -> become 1 -> still can walk thorugh
        #WARNING :You must cut off the trees in order from shortest to tallest.
        #it said must , its not optional
        #if it said all from small to big, them we need all bfs
        #ever=set()
        max_row=len(forest)
        max_column=len(forest[0])
        to_cut=dict()
        for row in range(len(forest)):
            for column in range(len(forest[0])):
                if forest[row][column]>1:
                    to_cut[forest[row][column]]=(row,column)
        srow=0
        scolumn=0
        went=set()
        sizeof=dict()
        meet=False
        answer=0
        def recursion(row,column):
            #get depth only
            nonlocal went, meet, answer,srow,scolumn,sizeof,tr,tc
            q=deque()
            while q:
                row,column=q.popleft()
                if meet:
                    return 0
                if not (0<=row<max_row and 0<=column<max_column):
                    return 0
                if (row,column) in went:
                    return 0
                went.add((row,column))
                if row==tr and column == tc:
                    #print(row,column)
                    answer+=sizeof[row,column]
                    #print(depth)
                    srow=row
                    scolumn=column
                    meet=True
                    return 0
                if forest[row][column]==0:
                    return 0
                for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                    q.append(row+a,column+b)
                    sizeof[(row+a,column+b)]=sizeof[(row,column)]
                
        for me in sorted(to_cut.keys()):
            tr,tc=to_cut[me]
            meet=False
            went=set()
            sizdof=defaultdict(int)
            recursion(srow,scolumn)
            #print(answer)
            if meet==False:
                return -1
        return answer
class Solution2:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        #more than 1: can cut -> become 1 -> still can walk thorugh
        #ever=set()
        max_row=len(forest)
        max_column=len(forest[0])
        def recursion(row=0,column=0):
            if not (0<=row<max_row and 0<=column<max_column):
                return -1
            #if in ever
            if forest[row][column]==0:
                return -1
            forest[row][column]=0
            #ever.add((row,column))
            #depth!=step , walk twice=child_depth+1
            count_child=0
            child_step=[]
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                bot=recursion(row+a,column+b)
                if bot>=0:
                    count_child+=1
                    child_step.append(bot)
            if len(child_step)==0:
                return 0
            if len(child_step)==1:
                return child_step[0]+1
            else:
                max_child=max(child_step)
                child_step.remove(max_child)
                count=max_child+1
                for rs in child_step:
                    count+=(rs+1)*2
                return count
        answer=recursion()
        for a in forest:
            for b in a:
                if b!=0:
                    return -1
        return answer
penter=Solution()
data=[[1,2,3],[0,0,4],[7,6,5]]
penter.cutOffTree(data)