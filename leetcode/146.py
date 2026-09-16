#did not finish
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.max_size=capacity
        self.queue=deque()
        self.now_size=0
        self.table=dict()
    def get(self, key: int) -> int:
        print("get",key)
        self.log()
        return self.table.get(key,-1)

    def put(self, key: int, value: int) -> None:
        print("before")
        self.log()
        if key in self.table:
            self.table[key]=value
        elif self.now_size<self.max_size:
            self.table[key]=value
            self.now_size+=1
            self.queue.append(key)
        else:
            self.table.pop(self.queue.popleft())
            self.queue.append(key)
            self.table[key]=value
        print("after")
        self.log()

    def log(self):
        print(self.table,list(self.queue))
    

    #we need to remove most not used element 