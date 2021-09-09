import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    adjs[i][j] = 0

    for _ in disr:
        new_i, new_j = i + _[0], j + _[1]
        if new_i < 0 or new_j < 0 or new_i >=N or new_j >=M:
            continue
        elif adjs[new_i][new_j] == 1:
            dfs(new_i, new_j)
    return


T = int(sys.stdin.readline())
disr = [(1,0), (-1,0), (0,1), (0, -1)]
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    adjs = [[0] * M for i in range(N)]
    warm_count = 0

    for j in range(K):
        V1, V2 = map(int, sys.stdin.readline().split())
        adjs[V2][V1] = 1

    for j in range(N):
        for k in range(M):
            if adjs[j][k] == 1:
                dfs(j, k)
                warm_count += 1
    print(warm_count)

