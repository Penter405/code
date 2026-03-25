"""
X組和Y組的所有科目
X組和Y組的共同科目
Y組有但X組沒有的科目
X組和Y組彼此沒有的科目（不包含相同科目）
"""
"""print(dir(list))
exit()
"""
x=set()
print("Enter group X's subjects:")
while 1:
    s=input()
    if s=="end":
        break
    x.add(s)

y=set()
print("Enter group Y's subjects:")
while 1:
    s=input()
    if s=="end":
        break
    y.add(s)

for rs in [x|y,x&y,y-x,x^y]:
    print(list(rs).sort())
