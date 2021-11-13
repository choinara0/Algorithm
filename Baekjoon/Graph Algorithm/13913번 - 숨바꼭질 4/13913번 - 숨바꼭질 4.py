import sys
from collections import deque

N, K = map(int ,sys.stdin.readline().split())

def bfs(n, k):
    max = 100001
    arr = [-1] * max
    path = [0] * 100001
    arr[n] = 0
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(arr[x])
            p = []
            while x != n:
                p.append(x)
                x = path[x]
            p.append(n)
            p.reverse()
            print(' '.join(map(str, p)))
            break
        for i in (x*2, x-1, x+1):
            if 0 <= i < max and arr[i] == -1:
                arr[i] = arr[x] + 1
                path[i] = x
                q.append(i)
    return

bfs(N, K)