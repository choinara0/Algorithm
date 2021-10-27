import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
check = [[-1, 0] for i in range(100001)]
check[N][0] = 0
check[N][1] = 1
q = deque()
q.append(N)

while q:
    x = q.popleft()

    for i in (x+1, x-1, x*2):
        if 0 <= i < 100001:
            if check[i][0] == -1:
                check[i][0] = check[x][0] + 1
                check[i][1] = check[x][1]
                q.append(i)
            elif check[i][0] == check[x][0] + 1:
                check[i][1] += check[x][1]

print(check[K][0])
print(check[K][1])
