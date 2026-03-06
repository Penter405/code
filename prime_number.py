dp=[2,3,5]#HASH TABLE, NOT DP

def is_prime(n):
    
    global dp
    #print(dp)
    if n in dp:
        return True
    for i in dp:
        if (n%i)==0:
            #not prime
            return False
    dp.append(n)
    return True

for n in range(2,101):
     #print(f"seeing {n}")
     if is_prime(n):
        (print(f"{n} prime "))
