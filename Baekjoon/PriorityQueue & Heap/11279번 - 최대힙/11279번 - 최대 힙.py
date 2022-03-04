# PriorityQueue 사용
import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
priorityQueue = PriorityQueue(maxsize=N)

for i in range(N):
    temp = -1 * int(sys.stdin.readline())
    if temp == 0 and priorityQueue.qsize() == 0:
        print(0)
    elif temp == 0 and priorityQueue.qsize() != 0:
        print(-1 * priorityQueue.get())
    else:
        priorityQueue.put(temp)

sys.exit()