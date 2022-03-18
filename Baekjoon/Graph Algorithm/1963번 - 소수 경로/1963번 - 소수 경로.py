import sys
from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    visited = [0] * 10000
    visited[a] = 1
    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt
        x = str(x)
        for i in range(4):
            for j in range(0, 10):
                temp = int(x[:i] + str(j) + x[i+1:])
                if not visited[temp] and temp>=1000 and prime_arr[temp]:
                    visited[temp] = 1
                    q.append([temp, cnt+1])
    return 'Impossible'

prime_arr = [True] * 10000
for i in range(2, 10000):
    if prime_arr[i]:
        for j in range(i*i, 10000, i):
            prime_arr[j] = False

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))