from collections import deque

def bfs(n, start, not_visit, graph):
    visited = [0] * (n+1)
    visited[not_visit] = 1
    visited[start] = 1
    result = 1
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                result += 1
                visited[i] = 1
                q.append(i)

    return result

def solution(n, wires):
    answer = n
    graph = [[]*(n+1) for _ in range(n+1)]
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    for start, not_visit in wires:
        result = bfs(n, start, not_visit, graph)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]) # 3
solution(4, [[1,2],[2,3],[3,4]]) # 0
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]) # 1
