import math
s=[48,120,60]
result=max(s)
for rs in s:
    result=math.gcd(result,rs)
print(result)