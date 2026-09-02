class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            if room not in never:
                #tooked
                return 0
            never.remove(room)
            for key in rooms[room]:
                dfs(key)
        never=set([i for i in range(len(rooms))])
        dfs(0)
        #for room in [i for i in range(len(rooms))]:
        #    dfs(room)
        print(never)
        return len(never)==0