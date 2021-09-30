import sys
N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(len(num)):
            if len(result) == 0:
                result.append(num[i])
                dfs()
                result.pop()
            elif result[-1] <= num[i]:
                result.append(num[i])
                dfs()
                result.pop()

dfs()