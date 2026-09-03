class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for rs in s:
            if len(stack)==0:
                stack.append(rs)
                continue
            if rs==stack[-1]:
                stack.pop(-1)
            else:
                stack.append(rs)
        return "".join(stack)