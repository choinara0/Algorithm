import sys
N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
result = []
visited = [False] * (N+1)

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(len(num)):
            if visited[i] == False:
                visited[i] = True
                result.append(num[i])
                dfs()
                visited[i] = False
                result.pop()

dfs()

            

