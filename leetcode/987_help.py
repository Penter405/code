def f_1():
    s=dict()
    while True:
        r=input()
        if r=="0":
            break
        a=input()
        s[r]=a


    for rs in sorted(s.keys()):
        print(rs,s[rs])
def f_2():
    help(list)
def f_3():
    a=[]
    print(a==None)
def f_4():
    s=[]
    s.extend(sorted([3]))
f_4()