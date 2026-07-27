#0:10:43 unfinished
#0:10:49 unfinished
#the shape is reversed N of juat h
#the shape is reversed N of juat h
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #3 1 3 1 to get first eleent
        if numRows==1:
            return s
        a=[]
        b=[]
        n_or_rever=1
        counter=0
        for rs in s:
            
            if n_or_ever==1:
                if counter==0:
                    a.append(list())
                a.append(rs)
                counter+=1
                if counter==numRows:
                    n_or_rever=0
                    counter=0
            else:
                if counter==0:
                    b.append(list())
                b.append(rs)
                counter+=1
                if counter>=numRows-2:
                    n_orrever=0
                    counter=0
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