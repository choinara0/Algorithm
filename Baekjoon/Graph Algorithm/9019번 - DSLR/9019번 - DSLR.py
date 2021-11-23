import sys
from collections import deque

T = int(sys.stdin.readline())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((x, ''))
    visited = [0] * 10001
    visited[x] = 1
    answer = ''
    while q:
        x, cmd = q.popleft()
        if x == y:
            answer = cmd
            break
        if 2 * x <= 9999 and not visited[2 * x]:
            q.append((2 * x, cmd + 'D'))
            visited[2 * x] = 1
        if 2 * x > 9999 and not visited[(2 * x) % 10000]:
            q.append(((2 * x) % 10000, cmd + 'D'))
            visited[(2 * x) % 10000] = 1
        if x - 1 >= 0 and not visited[x - 1]:
            q.append((x - 1, cmd + 'S'))
            visited[x - 1] = 0
        if x - 1 < 0 and not visited[9999]:
            q.append((9999, cmd + 'S'))
            visited[9999] = 1
        Lx = int((x % 1000) * 10 + x / 1000)
        if not visited[Lx]:
            q.append((Lx, cmd + 'L'))
            visited[Lx] = 1
        Rx = int((x % 10) * 1000 + x / 10)
        if not visited[Rx]:
            q.append((Rx, cmd + 'R'))
            visited[Rx] = 1

    print(answer)