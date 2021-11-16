import sys
from collections import deque

def solution(N, road, K):
    answer = 0
    streetMatrix = [[] for i in range(N+1)]
    for r in road:
        streetMatrix[r[0]].append([r[1], r[2]])
        streetMatrix[r[1]].append([r[0], r[2]])
    visited =  [sys.maxsize] * (N+1)
    visited[1] = 0
    q = deque()
    q.append((1, 0))
    while q:
        now, cnt = q.popleft()
        for i in streetMatrix[now]:
            if cnt+i[1] <= K and cnt + i[1] < visited[i[0]]:
                visited[i[0]] = cnt + i[1]
                q.append((i[0], cnt + i[1]))

    for i in visited:
        if i != sys.maxsize:
            answer += 1

    return answer

solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3) # 4
solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4) #4