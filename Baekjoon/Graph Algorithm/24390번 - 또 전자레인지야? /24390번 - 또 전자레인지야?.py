from heapq import *
from collections import deque
import sys

M, S = sys.stdin.readline().split(':')
T = int(M) * 60 + int(S)

cnt = 0
cnt += (T // 600)
T %= 600
cnt += (T // 60)
T %= 60
q = deque()
q.append([cnt, 0, False])

while q:
    c, t, flag = q.popleft()

    if t == T and flag:
        print(c)
        break

    for i in [10, 60, 600]:
        if i + t <= T:
            q.append([c+1, i+t, flag])
    if flag:
        if t + 30 <= T:
            q.append([c+1, 30+t, flag])
    else:
        if t + 30 <= T:
            q.append([c+1, 30+t, True])