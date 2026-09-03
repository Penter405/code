s=input().replace('-','')
bot=0
try:
    for rs in s:
        bot=int(s)
    print("Valid SSN")
except:
    print("Invalid SSN")