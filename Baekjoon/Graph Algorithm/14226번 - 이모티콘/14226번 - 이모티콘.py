import sys
from collections import deque

N = int(sys.stdin.readline())
emoji = [[-1 for i in range(N+1)] for j in range(N+1)]

def bfs(n):
    q = deque()
    q.append((1, 0))
    emoji[1][0] = 0
    answer = -1
    while q:
        s, c = q.popleft()
        if emoji[s][s] == -1:
            emoji[s][s] = emoji[s][c] + 1
            q.append((s, s))
        if s + c <= n and emoji[s + c][c] == -1:
            q.append((s + c, c))
            emoji[s + c][c] = emoji[s][c] + 1
        if s - 1 >= 0 and emoji[s - 1][c] == -1:
            q.append((s - 1, c))
            emoji[s - 1][c] = emoji[s][c] + 1

    for i in range(n+1):
        if emoji[n][i] != -1:
            if answer == -1 or answer > emoji[n][i]:
                answer = emoji[n][i]

    return answer

print(bfs(N))