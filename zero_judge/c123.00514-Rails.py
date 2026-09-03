cout=print
def print(n):
    pass

def is_stationable(to_be:list[int],size:int):
    before=[]
    for rs in range(size,0,-1):
        before.append(rs)
    buffer=[]
    go_to_solve_index=0
    while before or buffer:
        #print("before: ",before,'\n',"buffer: ",buffer,"\n to_be index: ",go_to_solve_index)
        if to_be[go_to_solve_index] in before:
            for rs in range(len(before)-1,before.index(to_be[go_to_solve_index]),-1):
                buffer.append(before.pop(-1))
            before.pop(-1)#now move the correct number to to_be, as to_be was pre add data, we just remove in list 'before'
        else:
            #in buffer
            if buffer[-1]==to_be[go_to_solve_index]:
                buffer.pop(-1)
            else:
                return "No"
        go_to_solve_index+=1
    return "Yes"
        
result=[]
do=1
while not(do==0 and sizeof==0):
    sizeof=int(input())
    if sizeof==0:
        break
    result.append([])
    while True:
        buffer=list(map(int,input().split()))
        print(buffer)#default split take all space between element that non-space
        if buffer==[0]:
            break
        result[-1].append(is_stationable((buffer),sizeof))

for rs in result:
    cout('\n'.join(rs))
    cout()