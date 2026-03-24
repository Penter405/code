"""
for s in ['A','Z','a','z','0','9']:
    print(ord(s))
"""
def small_letter(a):
    if ord(a)>=97 or ord(a)<=122:
        return True
    return False

def big_letter(a):
    if ord(a)>=65 or ord(a)<=90:
        return True
    return False

def integer(a):
    if ord(a)>=48 or ord(a)<=57:
        return True
    return False
"""
good
return "Valid password"



bad
return "Invalid password"
"""

def yes_no():
    s=input()
    if len(s)<8:
        return "Invalid password"
    is_any_big=0
    for rs in s:
        if not(small_letter(rs) or big_letter(rs) or integer(rs)):
            return "Invalid password"

        if big_letter(rs):
            is_any_big=1
    if is_any_big==0:
        return "Invalid password"
    return "Valid password"
    
print(yes_no())