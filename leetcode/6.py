#0:10:43 unfinished
#the shape is reversed N of juat h
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #3 1 3 1 to get first eleent
        a=[]
        b=[]
        ever=-1
        for rs in numRows:
            ever+=1
            if ever==3:
                b.append(rs)
                ever=-1
            if ever==0:
                a.append(list())
            a.append(rs)
            ever+=1
        result=[]
        for rs in range(len(a)):
            result.append(a[rs][0])
        is_a=1
        pa=0
        pb=0
        for rs in range(len(a)+len(b)):
            if is_a:
                result.append(a[pa][1])
                pa+=1
                is_a=0
            else:
                result.append(b[pb])
                is_a=1
                