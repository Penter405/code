k=int(input())
for f in range(k):
    s=list(map(float,input().split()))
    print(f"{max(s)-min(s):.2f}")