import sys

def dfs(start, cnt):
    global result
    if cnt == 6:

        print(' '.join(map(str, result)))
        return
    else:
        for i in range(start, len(num)):
            if visited[i] == False:
                if len(result) == 0 or result[-1] <= num[i]:
                    visited[i] = True
                    result.append(num[i])
                    dfs(start+1, cnt+1)
                    result.pop()
                    visited[i] = False

while True:
    num = list(map(int, sys.stdin.readline().split()))
    x = num.pop(0)
    result = []
    visited = [False] * (x + 1)
    if x == 0:
        break
    else:
        dfs(0, 0)
    print()