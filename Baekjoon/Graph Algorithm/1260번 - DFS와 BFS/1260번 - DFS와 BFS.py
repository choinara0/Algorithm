from collections import deque
def dfs(start_node):
    visited_dfs[start_node] = 1
    print(start_node, end=" ")
    for i in range(1, N+1):
        if visited_dfs[i] == 0 and matrix[start_node][i] == 1:
            dfs(i)
    return

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited_bfs[start_node] = 1
    while(queue):
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, N+1):
            if visited_bfs[i] == 0 and matrix[v][i] == 1:
                queue.append(i)
                visited_bfs[i] = 1
    return

N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b= map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

dfs(V)
print()
bfs(V)

