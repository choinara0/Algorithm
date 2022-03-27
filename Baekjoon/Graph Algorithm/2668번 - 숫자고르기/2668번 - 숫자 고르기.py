import sys

def dfs(v, i):
    visited[v] = 1

    for n in graph[v]:
        if not visited[n]:
            dfs(n, i)
        elif visited[n] and n == i:
            answer.append(n)

N = int(sys.stdin.readline())
graph = [[]*(N+1) for i in range(N+1)]
answer = []
for i in range(1, N+1):
    graph[int(sys.stdin.readline())].append(i)

for i in range(1, N+1):
    visited = [0] * (N + 1)
    dfs(i, i)

print(len(answer))
print('\n'.join(map(str, answer)))