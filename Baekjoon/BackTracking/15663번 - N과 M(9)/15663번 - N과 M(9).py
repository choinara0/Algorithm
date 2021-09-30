import sys
N, M = map(int ,sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
result = []
visited = [False] * (N+1)
check = {}
def dfs():

    if len(result) == M :
        s = ' '.join(map(str, result))
        if s not in check:
            check[s] = 1
            print(s)
            return
    else:
        for i in range(len(num)):
            if visited[i] == False:
                visited[i] = True
                result.append(num[i])
                dfs()
                result.pop()
                visited[i] = False

dfs()

