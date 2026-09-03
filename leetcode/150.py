"""
#print(help(list.pop))
print(int(-3.99))
print(int(3.66))
"""
s={'+','-','*','/'}
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #operator will do things for lastest two integer;
        stack=[]
        #print(type(s))
        for rs in tokens:
            if len(stack)==0:
                stack.append(rs)
                continue
            if rs in s:
                last=stack.pop()
                first=stack.pop()
                #print(f"take off {first} and {last},",end='  ')
                #print(int(eval(f"{first}{rs}{last}")),end=' = ')
                #print(f"{first}{rs}{last}")
                stack.append(int(eval(f"{first}{rs}{last}")))
            else:
                stack.append((rs))

            
        return int(stack[0])