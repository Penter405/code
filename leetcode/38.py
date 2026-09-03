class Solution:
    def do(self,it):
        new_it=""
        last_element="-1"
        repeated=0
        for rs in it:
            if rs != last_element and last_element!="-1":
                new_it+=str(repeated)
                new_it+=last_element
                repeated=1
            else:
                repeated+=1
            last_element=rs
        if repeated:
            new_it+=str(repeated)
            new_it+=last_element
        return new_it
    def countAndSay(self, n: int) -> str:
        result="1"
        for rs in range(n-1):
            result=self.do(result)
            print(result)
        return result