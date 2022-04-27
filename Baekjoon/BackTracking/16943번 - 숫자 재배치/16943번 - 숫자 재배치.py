import sys

def dfs(cnt, sum_val):
    global answer

    if cnt == len_a:
        if int(sum_val) <= b:
            answer = max(answer, int(sum_val))
            return
    for i in range(len_a):
        if cnt == 0 and a[i] == 0:
            continue
        if not check[i]:
            check[i] = True
            dfs(cnt+1, sum_val + str(a[i]))
            check[i] = False

    return

a, b = map(int, sys.stdin.readline().split())
a = list(map(int, str(a)))
len_a = len(a)
check = [False] * len_a
answer = -1
dfs(0, '')
print(answer)