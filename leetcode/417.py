#0:33:35
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #represents the height above sea level of the cell at coordinate (r, c)
        #can move if neighboring cell's height is less than or equal to the current cell's height.
        #if we higher or same than friend, flow
        #a node can higher continously to left top side cells and botton right side cells
        pa_able=set()
        at_able=set()
        #&
        def is_pa(row,column):
            if row==0 or column==0:
                return 1
            return 0
        def is_at(row,column):
            if row==len(heights) or column==len(heights[0]):
                return 1
            return 0
        def out(row,column):
            if 0<=row<len(heights) and 0<=column<len(heights[0]):
                return 0
            return 1
        """
        pa_list=[]
        at_list=[]
        pa_list.extend((heights[0]))
        for rs in range(len(heights[0])):
            pa_list.append()
        """
        def bfs(row,column,me_able):
            if out(row,column):
                return 0
            if (row,column) in me_able:
                return 0
            me_able.add((row,column))
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                if out(row+a,column+b)==0 and heights[row][column]<=heights[row+a][column+b]:
                    bfs(row+a,column+b,me_able)
        for rs in range(len(heights[0])):
            bfs(0,rs,pa_able)
        for rs in range(len(heights)):
            bfs(rs,0,pa_able)
        for pe in range(len(heights[0])):
            bfs(len(heights)-1,pe,at_able)
        for pe in range(len(heights)):
            bfs(pe,len(heights[0])-1,at_able)
        print(pa_able,at_able)
        return list(pa_able & at_able)