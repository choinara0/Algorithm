import sys
N, p_e, p_w, p_s, p_n = map(int, sys.stdin.readline().split())
percentage = [p_e/100, p_w/100, p_s/100, p_n/100]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
visited = {(0, 0)}
def dfs(x, y, cnt, prob):
    global ans

    if cnt == N:
        ans += prob
        return

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if (new_x, new_y) not in visited:
            visited.add((new_x, new_y))
            dfs(new_x, new_y, cnt+1, prob*percentage[i])
            visited.remove((new_x, new_y))

dfs(0, 0, 0, 1)
print(ans)