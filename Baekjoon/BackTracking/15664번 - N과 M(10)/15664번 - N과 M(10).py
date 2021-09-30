import sys

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
result = []
check = {}
visited = [False] * (N+1)

def dfs():
    if len(result) == M:
        s = ' '.join(map(str, result))
        if s not in check:
            check[s] = 1
            print(s)
        return
    else:
        for i in range(len(num)):
            if visited[i] == False:
                if len(result) == 0 or result[-1] <= num[i]:
                    visited[i] = True
                    result.append(num[i])
                    dfs()
                    result.pop()
                    visited[i] = False

dfs()
