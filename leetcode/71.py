class Solution:
    def __init__(self):
        self.buffer=[]
        self.stack=[]
    def from_buffer_to_stack(self):
        if self.buffer:
            b2=''.join(self.buffer)
            self.buffer=[]
            if b2=="..":
                if self.stack:
                    self.stack.pop(-1)
            elif b2==".":
                pass
            else:
                self.stack.append(b2)
    def simplifyPath(self, path: str) -> str:
        #stack=[]
        #stack.pop(-1)
        #exit()
        s=path.split('/')
        #buffer=[]
        for i in range(1,len(path)):
            if path[i]=='/':
                self.from_buffer_to_stack()
            else:
                self.buffer.append(path[i])
        self.from_buffer_to_stack()
        print(('/'.join(self.stack)))
        return "/"+('/'.join(self.stack))