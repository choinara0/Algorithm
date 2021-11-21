import sys
N = int(sys.stdin.readline())
energy = list(map(int, sys.stdin.readline().split()))
maxAns = float('-Inf')
def dfs(temp, li):
    global maxAns
    if len(li) == 2:
        if temp > maxAns:
            maxAns = temp
            return

    for i in range(1, len(li)-1):
        r = li[i-1] * li[i+1]
        templi = li[i]
        del li[i]
        dfs(temp + r, li)
        li.insert(i, templi)


dfs(0, energy)
print(maxAns)