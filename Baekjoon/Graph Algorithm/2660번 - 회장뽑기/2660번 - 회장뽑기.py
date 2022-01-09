#플로이드-워셜(Floyld-Warshall)

import sys

n = int(sys.stdin.readline())
arr = [[sys.maxsize for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
    arr[i][i] = 0

while 1:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

ans, res = [], []
for i in range(1, n+1):
    ans.append(max(arr[i][1:n+1]))
minAns = min(ans)
print(minAns, ans.count(minAns))

for i in range(0, n):
    if ans[i] == minAns:
        res.append(i+1)
print(*res)