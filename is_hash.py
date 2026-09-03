objects = [int, str, float, bool, list, tuple, dict, set]
for obj in objects:
    if "__hash__" in dir(obj) :
        bot=""
    else:
        bot="not "
    if "__eq__" in dir(obj) :
        bot2=""
    else:
        bot2="not "
    print(f"{obj.__name__} has {bot}__hash__ method, has {bot2}__eq__ method.")

def cout_all():
    print(int)
    print(dir(int))
    print(str)
    print(dir(str))
    print(float)
    print(dir(float))
    print(bool)
    print(dir(bool))
    print(list)
    print(dir(list))
    print(tuple)
    print(dir(tuple))
    print(dict)
    print(dir(dict))
    print(set)
    print(dir(set))
cout_all()