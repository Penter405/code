class Solution:
    def __init__(self):
        self.result=0
        self.hight=0
    def recursion(self, num, hight):
        print(num, hight)
        if num==0:
            return 0
        if hight==self.hight:
            if self.result==0:
                self.result=(num)
            else:
                if self.result>(num):
                    self.result=(num)
            return 0
        for rs in range(len(str(num))):
            bot=list(str(num))
            bot.pop(rs)
            self.recursion(int(''.join(bot)),hight+1)
    def removeKdigits(self, num: str, k: int) -> str:
        self.hight=k
        self.recursion(int(num),0)
        return str(self.result)\