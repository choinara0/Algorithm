import sys
from collections import deque

LIMIT = 100001

def solution(time, N, K):
    q = deque()
    q.append(N)

    while q:
        temp = q.popleft()

        if temp == K:
            return time[temp]

        for i in (temp+1, temp-1, 2*temp):
            if (0 <= i < LIMIT) and time[i] == 0:
                time[i] = time[temp] + 1
                q.append(i)



N, K = map(int, sys.stdin.readline().split())
time = [0] * LIMIT
print(solution(time, N, K))




