def dfs(start, visited):
    visited[start] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and matrix[start][i] == 1:

            global num
            num += 1
            dfs(i, visited)
    return

N = int(input())
matrix = [[0]*(N+1) for i in range(N+1)]
# print(matrix)
for i in range(int(input())):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


visited = [0] * (N+1)
num = 0
dfs(1, visited)
print(num)




