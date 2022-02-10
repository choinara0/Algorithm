from collections import deque

def solution(n, results):
    answer = 0
    win_graph = [[] for i in range(n+1)]
    lose_graph = [[] for i in range(n+1)]

    for r in results:
        win_graph[r[0]].append(r[1])
        lose_graph[r[1]].append(r[0])

    for i in range(1, n+1):
        visited = [0] * (n+1)
        visited[0] = visited[i] = 1
        for nodes in [win_graph, lose_graph]:
            q = deque([i])
            while q:
                idx = q.popleft()
                for node in nodes[idx]:
                    if not visited[node]:
                        visited[node] = 1
                        q.append(node)

        if 0 not in visited:
            answer += 1
    return answer

# solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]) # 2