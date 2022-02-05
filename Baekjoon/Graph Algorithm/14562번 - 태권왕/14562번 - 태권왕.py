import sys
from collections import deque

C = int(sys.stdin.readline())
def bfs(s, t):
    q = deque()
    q.append((s, t, 0))
    while q:
        x, y, cnt = q.popleft()
        if x <= y:
            q.append((2*x, y+3, cnt+1))
            q.append((x+1, y, cnt+1))
            if x == y:
                return cnt


for _ in range(C):
    S, T = map(int, sys.stdin.readline().split())
    print(bfs(S, T))