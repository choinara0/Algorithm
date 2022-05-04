import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(arr):
    start = arr[0]
    q = deque()
    q.append(start)
    visited = set([start])
    num = 0

    while q:
        value = q.popleft()
        num += people[value]
        for i in graph[value]:
            if i not in visited and i in arr:
                q.append(i)
                visited.add(i)

    return num, len(visited)

N = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
result = sys.maxsize

for i in range(1, N+1):
    graph[i] = list(map(int, input().split()))
    graph[i] = graph[i][1:]

for i in range(1, N//2+1):
    combies = list(combinations(range(1, N+1), i))
    for comb in combies:
        sum1, temp1 = bfs(comb)
        sum2, temp2 = bfs([i for i in range(1, N+1) if i not in comb])

        if temp1 + temp2 == N:
            result = min(result, abs(sum1 -sum2))

if result != sys.maxsize:
    print(result)
else:
    print(-1)