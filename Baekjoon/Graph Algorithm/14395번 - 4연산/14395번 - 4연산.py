import sys
from collections import deque

s, t = map(int, sys.stdin.readline().split())
visited = set()

def bfs(x):
    q = deque()
    q.append((x, ''))
    visited.add(x)

    while q:
        x, op_list = q.popleft()

        if x == t:
            return op_list

        for o in ('*', '+', '/'):
            if o == '*':
                nx = x * x
            elif o == '+':
                nx = x + x
            else:
                nx = 1
            if 0<=nx<=t and nx not in visited:
                q.append((nx, op_list + o))
                visited.add(nx)

    return -1

if s == t:
    print(0)
else:
    print(bfs(s))
