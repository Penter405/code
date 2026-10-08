import random
"""
before_random=[
2787, 3-1        done
2707,  5-2       done
188,3573,  6-1  , 188 done
3259,376,  6-2
3628  6-3
]


"""
#help(random)
data=[3840,2140,152,3393,931,3603,2304,2915,1774,518,279,3592,1155,583,712,72,718,3290,115,97,1092,44,10,334,354,139,91,639,123,309,714,2222,2708]
sizeof=len(data)
for _ in range(sizeof):
    rs=random.choice(data)
    data.remove(rs)
    print(rs)