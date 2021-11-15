from collections import deque

def solution(n, edge):
    graph = [[]*(n+1) for i in range(n+1)]
    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    cost = [0] * (n+1)
    cost[1] = 1
    q = deque()
    q.append((1, 0))
    while q:
        idx, cnt = q.popleft()
        for i in graph[idx]:
            if cost[i] == 0:
                q.append((i, cnt + 1))
                cost[i] = cost[idx] + 1
    answer = 0
    maxCost = max(cost)
    for i in cost:
        if i == maxCost:
            answer += 1

    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) #3