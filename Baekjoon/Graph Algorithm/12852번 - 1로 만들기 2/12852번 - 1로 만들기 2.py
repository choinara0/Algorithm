import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
def bfs(n):
    q = deque()
    q.append([n])

    while q:
        arr = q.popleft()
        x = arr[-1]
        if x == 1:
            answer = arr
            return answer
        if x%3 == 0:
            q.append(arr + [x//3])
        if x%2 == 0:
            q.append(arr + [x//2])
        q.append(arr + [x-1])

    return
if N == 1:
    print(0)
    print(1)
else:
    answer = bfs(N)
    print(len(answer)-1)
    print(*answer)
