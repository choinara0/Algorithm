import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs():
    q = deque()
    q.append((home_x, home_y))

    while q:
        x, y = q.popleft()
        if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = convenience_store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append((nx, ny))
                    visited[i] = 1
    print('sad')
    return

for _ in range(t):
    n = int(sys.stdin.readline())
    home_x, home_y = map(int,sys.stdin.readline().split())
    convenience_store = []
    for i in range(n):
        convenience_store.append(list(map(int, sys.stdin.readline().split())))
    festival_x, festival_y = map(int, sys.stdin.readline().split())
    visited = [0] * (n+1)
    bfs()