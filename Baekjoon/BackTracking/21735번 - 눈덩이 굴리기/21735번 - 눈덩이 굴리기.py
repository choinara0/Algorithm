import sys

def dfs(time, idx, size):
    global answer

    if time > M :
        return

    if time <= M:
        answer = max(size, answer)

    for i in (1, 2):
        if i + idx >= len(a):
            continue
        if i == 1:
            dfs(time+1, idx+i, size + a[idx+i])
        else:
            dfs(time+1, idx+i, (size//2) + a[idx+i])

    return

N, M = map(int, sys.stdin.readline().split())
a = [0] + list(map(int, sys.stdin.readline().split()))
answer = 0
dfs(0, 0, 1)
print(answer)