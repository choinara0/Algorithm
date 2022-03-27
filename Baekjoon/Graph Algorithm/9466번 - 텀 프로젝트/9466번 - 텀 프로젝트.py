import sys
sys.setrecursionlimit(10**7)
T = int(sys.stdin.readline())

def dfs(x):
    global cycle
    visited[x] = 1
    temp_cycle.append(x)
    num = student_list[x]

    if visited[num]:
        if num in temp_cycle:
            cycle += temp_cycle[temp_cycle.index(num):]
        return
    else:
        dfs(num)

for _ in range(T):
    n = int(sys.stdin.readline())
    student_list = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n+1)
    cycle = []

    for i in range(1, n+1):
        if not visited[i]:
            temp_cycle = []
            dfs(i)

    print(n-len(cycle))