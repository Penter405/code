from collections import deque
print(dir(deque))
#help(deque)
q=deque()
q.append(1)
q.popleft()
print(q)