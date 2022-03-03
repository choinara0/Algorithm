# heapq 사용해서 우선순위 큐 만들기
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
card = []
card_list = list(map(int, sys.stdin.readline().split()))

for i in card_list:
    heapq.heappush(card, i)

for j in range(M):
    card1 = heapq.heappop(card)
    card2 = heapq.heappop(card)
    sumCard = card1 + card2

    heapq.heappush(card, sumCard)
    heapq.heappush(card, sumCard)

print(sum(card))

# priorityqueue 사용
'''
import sys
from queue import PriorityQueue

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
priorityQueue = PriorityQueue()
result = 0
for i in range(N):
    priorityQueue.put(num[i])

for j in range(M):
    temp1 = priorityQueue.get()
    temp2 = priorityQueue.get()
    sumTemp = temp1 + temp2
    priorityQueue.put(sumTemp)
    priorityQueue.put(sumTemp)

for i in range(priorityQueue.qsize()):
    result += priorityQueue.get()

print(result)
'''