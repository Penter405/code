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