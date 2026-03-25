"""print(dir(dict))
exit()"""
print("Create dict1:")
dic_1=dict()
while 1:
    key=input("Key: ")
    if key=="end":
        break
    value=input("Value: ")
    dic_1[key]=value
dic_2=dict()
print("Create dict2:")
while 1:
    key=input("Key: ")
    if key=="end":
        break
    value=input("Value: ")
    dic_2[key]=value
dic_1.update(dic_2)
#print(dic_1)
for i in sorted(dic_1):
    print(f"{i}: {dic_1[i]}")