"""
x軸, caller from:global, local, double local
y軸, callee to: global, local, double local
y軸itself:mutable, immutable
r軸:name hit, name not same

3x3x2x2=36 cases
"""
"""
if variable defined in indentation of self function:
    the name will be compile, name always own by the function
else:
    search from local (if search it difined in local, run row 11)>>nonlocal>>global>>built in
"""


mutable=[]
immutable=3
def call_global_in_function():
    try:
        print(mutable)
        print("local can call global mutable")#
    except:
        print("local cant call global mutable")
    try:
        print(immutable)
        print("local can call global immutable")#
    except:
        print("local can not call global immutable")


def call_global_in_functions():
    def inner_function():
        print("running inner function")
        try:
            print(mutable)
            print("double local can call global mutable")#
        except:
            print("double local cant call global mutable")
        try:
            print(immutable)
            print("double local can call global immutable")#
        except:
            print("double local can not call global immutable")
    inner_function()


def call_same_name_local_to_other():
    try:
        if mutable ==[]:
            print("mutable   name hit,local difined next row, same indentation, global,nonlocal,built in win")
        else:
            print("mutable   name hit,local difined next row, same indentation, local in win")
    except:
        print("mutable   name was taken by local in this function, like 'int a;'")#
    try:
        if immutable == 3:
            print("immutable name hit,local difined next row, same indentation, global,nonlocal,built in win")
        else:
            print("immutable name hit,local difined next row, same indentation, local in win")
    except:
        print("immutable name was taken by local in this function, like 'int a;'")#
    mutable=[3]
    immutable=5
    if mutable ==[]:
        print("mutable name hit, global,nonlocal,built in win")
    else:
        print("mutable name hit, local win")#
    if immutable ==3:
        print("immutable name hit, global,nonlocal,built in win")
    else:
        print("immutable name hit, local win")#

def call_same_name_local_to_other_with_tell_use_global():
    global mutable, immutable
    print("telling to use global")
    try:
        if mutable ==[]:
            print("mutable   name hit,told its global, same indentation, global,nonlocal,built in win")#
        else:
            print("mutable   name hit,told its global, same indentation, local in win")
    except:
        print("mutable   name was taken by local in this function, like 'int a;'")
    try:
        if immutable == 3:
            print("immutable name hit,told its global, same indentation, global,nonlocal,built in win")#
        else:
            print("immutable name hit, told its global, same indentation, local in win")
    except:
        print("immutable name was taken by local in this function, like 'int a;'")
    mutable=[3]
    immutable=5
    if mutable ==[3]:
        print("mutable name hit, global,nonlocal,built in win")
    else:
        print("mutable name hit, local win")
    if immutable ==5:
        print("immutable name hit, global,nonlocal,built in win")
    else:
        print("immutable name hit, local win")

#call_global_in_function()
#call_global_in_functions()
call_same_name_local_to_other()
call_same_name_local_to_other_with_tell_use_global()