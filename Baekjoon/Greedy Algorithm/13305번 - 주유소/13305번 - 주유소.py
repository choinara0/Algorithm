import sys
N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
answer = 0
minCost = cost[0]

for i in range(N-1):
    if minCost > cost[i]:
        minCost = cost[i]
    answer += (minCost * dist[i])

print(answer)