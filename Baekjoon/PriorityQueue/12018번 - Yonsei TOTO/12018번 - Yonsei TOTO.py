import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
answer = 0
temp = []
for i in range(n):
    p, l = map(int, sys.stdin.readline().split())
    mileageList = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(mileageList)

    num = p - l

    if num < 0:
        heapq.heappush(temp, 1)
    else:
        for i in range(num):
            heapq.heappop(mileageList)
        heapq.heappush(temp, heapq.heappop(mileageList))

while temp:
    minMileage = heapq.heappop(temp)
    if m-minMileage >= 0:
        answer += 1
        m = m-minMileage
    else:
        break

print(answer)