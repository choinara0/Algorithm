import sys
sys.setrecursionlimit(10**5)

def dfs(x):
    global cycle
    visited[x] = 1
    temp_cycle.append(x)
    num = graph[x]

    if visited[num]:
        if num in temp_cycle:
            cycle += temp_cycle[temp_cycle.index(num):]
        return
    else:
        dfs(num)

N = int(sys.stdin.readline())
graph = [0]
for _ in range(N):
    graph.append(int(sys.stdin.readline()))

visited = [0] * (N+1)
cycle = []

for i in range(1, N+1):
    if not visited[i]:
        temp_cycle = []
        dfs(i)
cycle.sort()
print(len(cycle))
print('\n'.join(map(str, cycle)))