import sys

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
result = []
check = {}

def dfs():
    if len(result) == M:
        s = ' '.join(map(str, result))
        if s not in check:
            check[s] = 1
            print(s)
        return
    else:
        for i in range(len(num)):
            if len(result) == 0 or result[-1] <= num[i]:
                result.append(num[i])
                dfs()
                result.pop()

dfs()