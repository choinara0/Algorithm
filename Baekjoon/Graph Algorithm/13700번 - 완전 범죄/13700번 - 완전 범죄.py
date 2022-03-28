import sys
from collections import deque

def bfs():
    q = deque()
    q.append([S, 0])
    visited = [0] * (N+1)
    visited[S] = 1
    for i in police:
        visited[i] = 1

    while q:
        x, cnt = q.popleft()
        if x == D:
            return cnt
        for dx in moves:
            nx = x + dx
            if 1<=nx<N+1 and not visited[nx]:
                q.append([nx, cnt+1])
                visited[nx] = 1

    return "BUG FOUND"

N, S, D, F, B, K = map(int, sys.stdin.readline().split())
police = list(map(int, sys.stdin.readline().split()))
moves = [F, -B]
answer = bfs()
print(answer)