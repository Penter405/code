"""print(dir(set))
help(set)
"""
for _ in range(int(input())):
    print(len(set(input().lower().replace(' ','')))==26)