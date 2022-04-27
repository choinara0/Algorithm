import sys

def dfs(sum_num, string):
    global cnt

    if sum_num > n:
        return
    if sum_num == n:
        cnt += 1
        if cnt == k:
            print(string[:-1])
            exit()
            return
    for i in (1, 2, 3):
        dfs(sum_num + i, string + str(i) + "+")

    return

n, k = map(int, sys.stdin.readline().split())
cnt = 0
dfs(0, '')
print(-1)