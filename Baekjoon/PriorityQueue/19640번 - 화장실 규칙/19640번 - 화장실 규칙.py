import sys
from queue import PriorityQueue
from collections import deque

N, M, K = map(int ,sys.stdin.readline().split())
watingQueue = [deque() for i in range(M)]
index = 0
for i in range(N):
    lineNum = index%M
    Di, Hi = map(int, sys.stdin.readline().split())
    watingQueue[lineNum].append((Di*-1, Hi*-1, lineNum, i+1))
    index += 1

outputQueue = PriorityQueue()
w, cnt = -1, -1
for i in range(M):
    if watingQueue[i]:
        outputQueue.put(watingQueue[i].popleft())

while w != (K+1):
    d, h, outputLine, w = outputQueue.get()
    cnt += 1
    if watingQueue[outputLine]:
        next_worker = watingQueue[outputLine].popleft()
        outputQueue.put(next_worker)

print(cnt)


