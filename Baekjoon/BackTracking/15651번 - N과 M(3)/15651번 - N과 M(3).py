import sys
N, M = map(int, sys.stdin.readline().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(1, N+1):
            result.append(i)
            dfs()
            result.pop()
    return

dfs()