import sys
from collections import deque
A, B, C = map(int, sys.stdin.readline().split())
check = [[0]*201 for i in range(201)]
answer = [0 for i in range(201)]

def bfs(a, b, c):
    q = deque()
    q.append((0, 0, c))
    while q:
        x, y, z = q.popleft()
        if check[x][y] == 1:
            continue
        check[x][y] = 1
        if x == 0:
            answer[z] = 1
        if x + y > b:
            q.append((x+y-b, b, z))
        else:
            q.append((0, x+y, z))
        if x + z > c:
            q.append((x+z-c, y, c))
        else:
            q.append((0, y, x+z))
        if y + x > a:
            q.append((a, y+x-a, z))
        else:
            q.append((y+x, 0, z))
        if y + z > c:
            q.append((x, y+z-c, c))
        else:
            q.append((x, 0, y+z))
        if z + x > a:
            q.append((a, y, z+x-a))
        else:
            q.append((z+x, y, 0))
        if z + y > b:
            q.append((x, b, z+y-b))
        else:
            q.append((x, z+y, 0))



bfs(A, B, C)
for i in range(201):
    if answer[i]:
        print(i, end=' ')