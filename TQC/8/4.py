#print(dir(str))
s=input()
print(s.upper())
#print(s)
s=s.split()
#print(s)
for i in range(0,len(s)):
    s[i]=(s[i][0].upper())+s[i][1:]

print(" ".join(s))