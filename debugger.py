def recursion(x):
    c=f"hi {x}"
    if x == 1:
        return 1
    elif x == 0:
        return 0
    return recursion(x-1)+recursion(x-2)

recursion(5)
print("done1")
print("done2")