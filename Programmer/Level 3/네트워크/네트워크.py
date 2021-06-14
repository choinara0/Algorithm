def dfs(v, n, computers, visited):
    visited[v] = 1
    for j in range(n):
        if j != v and computers[j][v] == 1 and visited[j] == 0:
            dfs(j, n, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i]==0:
            dfs(i, n, computers, visited)
            answer += 1
    print(answer)
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])