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
            elif len(result) >= 1:
                x = result.pop()
                if i >= x:
                    result.append(x)
                    result.append(i)
                    dfs()
                    result.pop()
                else:
                    result.append(x)


dfs()
