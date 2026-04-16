
import sys
sys.set_int_max_str_digits(0)
x=1
print("doing")
for i in range(1, 9999):
    x*=i
    #print(x)
print(len(str(x)))
print("done")