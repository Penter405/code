class node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def init():
    result=[]
    while 1:
        x,l,r=list(map(str,input().split()))
        if x=="stop":
            break
        x=node(int(x))
        result.append(x)
        if l!="-":
            l=node(int(l))
            x.left(l)
            result.append(l)
            print(id(x.left)==id(l))
        if r!="-":
            r=node(int(r))
            x.left(r)
            result.append(r)
            print(id(x.right)==id(r))
        
    return result[0]

