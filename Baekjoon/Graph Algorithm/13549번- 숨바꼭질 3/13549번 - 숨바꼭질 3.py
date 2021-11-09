import sys
from collections import deque

N, K = map(int ,sys.stdin.readline().split())

def bfs(n, k):
    max = 100001
    arr = [-1] * max
    arr[n] = 0
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(arr[x])
            break
        for i in (x*2, x-1, x+1):
            if 0 <= i < max and arr[i] == -1:
                if i == 2*x:
                    arr[i] = arr[x]
                    q.appendleft(i)
                else:
                    arr[i] = arr[x] + 1
                    q.append(i)
    return

bfs(N, K)