import sys
from collections import deque

n = int(sys.stdin.readline())
stepping_stone = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline()) - 1
visited = [0] * n
answer = 0

def bfs(x):
    global answer
    q = deque()
    q.append(x)
    visited[x] = 1
    answer += 1

    while q:
        x = q.popleft()
        for i in [-stepping_stone[x], stepping_stone[x]]:
            nx = x + i
            if 0<=nx<n and not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                answer += 1

    return answer

print(bfs(s))