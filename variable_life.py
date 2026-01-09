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
        mutable.append(1)
        print("local can call global mutable")
    except:
        print("local cant call global mutable")
    try:
        immutable += 1
        print("local can call global immutable")
    except:
        print("local can not call global immutable")

#call_global_in_function()
def call_global_in_functions():
    def inner_function():
        print("running inner function")
        try:
            mutable.append(1)
            print("double local can call global mutable")
        except:
            print("double local cant call global mutable")
        try:
            immutable += 1
            print("double local can call global immutable")
        except:
            print("double local can not call global immutable")
    inner_function()

call_global_in_functions()