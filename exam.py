#accll number - letter
letter=input()
ascll_number=ord(letter)# ord == ordinal, which means index of iterable
letter=chr(ascll_number)# chr == char, which means character
#f-string
s=input()
print(f"|{s:<10}|")#s on left
print(f"|{s:^10}|")#s on middle
print(f"|{s:>10}|")#s on right
print(f"{3.1:.2f}")#3.10

#set method and operator
a=set(input())
b=set(input())
a|b#element in a or b
a&b#element in a and b
a-b#element in a but not in b
a^b#element in a or b, but not sametime in a and b

#mutable object passing by
list.sort#in place
sorted(reverse=False)#default from small to big, which is False , return sorted iterator

#reverse matrix
matrix=[]
matrix=[list(row) for row in zip(*matrix)][::-1]