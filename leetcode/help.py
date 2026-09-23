dp=[[],[(5,{1,2,3}),(20,{1,2,3})]]
got_free=[]
for all_in_this_cost in dp:
    print(all_in_this_cost)
    if len(all_in_this_cost)==0:
        got_free.append(0)
    else:
        got_free.append(max(all_in_this_cost)[0])

print(got_free)