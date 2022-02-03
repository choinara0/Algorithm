import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited = [-1] * (N+1)
dist_ans, count_ans, min_ans = float('-Inf'), float('Inf'), 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    global dist_ans, count_ans, min_ans
    q = deque()
    q.append((x, 0))
    visited[x] = 0
    while q:
        x, cnt = q.popleft()
        if dist_ans < cnt:
            min_ans = x
            dist_ans = cnt
            count_ans = 1
        elif dist_ans == cnt:
            min_ans = min(min_ans, x)
            count_ans += 1
        for node in graph[x]:
            if visited[node] == -1:
                q.append((node, cnt+1))
                visited[node] = visited[x] + 1

    return

bfs(1)
print(min_ans, dist_ans, count_ans)