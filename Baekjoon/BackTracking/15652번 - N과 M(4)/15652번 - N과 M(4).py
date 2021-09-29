import sys

N, M = map(int, sys.stdin.readline().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(1, N+1):
            if len(result) == 0:
                result.append(i)
                dfs()
                result.pop()
            elif result[-1] <= i:
                result.append(i)
                dfs()
                result.pop()

dfs()
