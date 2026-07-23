from collections import defaultdict,deque
class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        max_row=len(grid)
        max_column=len(grid[0])
        belong=dict()#tuple index to number x island
        new_island_number=0
        index_to_number=dict()
        land_size=defaultdict(int)
        relation_ship=dict()
        ever_if_bridge=1
        went=set()
        max_size=len(grid)
        """
        do multiple bfs or dfs, and if a node get 2 direction connect 2 island, 
        then save them, process after full traval
        
        
        """
        def bfs(row=0,column=0,number=None):
            if not(0<=row<max_size and 0<=column<max_size):
                return 0
            if (row,column) in belong:
                return 0
            if (grid[row][column]) == 0:
                return 0
            belong[(row,column)]=number
            land_size[number]+=1
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                bfs(row+a,column+b,number)
        def get_reation_and_land_size():
          number=0
          for row in range(max_row):
               for column in range(max_column):
                    if grid[row][column]==0:
                         for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                            if 0<=row+a<max_row and 0<=column+b<max_column:
                                if grid[row+a][column+b]==1:
                                    if (row,column) not in relation_ship:
                                        relation_ship[(row,column)]=[]
                                    relation_ship[(row,column)].append((row+a,column+b))
                    else:
                        if (row,column) not in belong:
                            number+=1
                            bfs(row,column,number)
        get_reation_and_land_size()
        #print(relation_ship)
        #print(land_size)
        for single_land in land_size.values():
            if single_land>ever_if_bridge:
                ever_if_bridge=single_land
        for key_point in relation_ship:
            if_now_bridge=1
            went_bridge=set()
            for rs in set(relation_ship[key_point]):
                if belong[rs] not in went_bridge:
                    if_now_bridge+=land_size[belong[rs]]
                    went_bridge.add(belong[rs])
            if if_now_bridge>ever_if_bridge:
                ever_if_bridge=if_now_bridge
        return ever_if_bridge

data=[[1,1],[1,1]]
penter=Solution()
print(penter.largestIsland(data))
        