import sys
import heapq

N, H, T = map(int, sys.stdin.readline().split())
height_heap = []
count = 0

for _ in range(N):
    heapq.heappush(height_heap, -int(sys.stdin.readline()))

for _ in range(T):
    max_height = heapq.heappop(height_heap)
    if abs(max_height) < H:
        break
    elif abs(max_height) == 1:
        heapq.heappush(height_heap, max_height)
    else:
        max_height = -(abs(max_height) // 2)
        heapq.heappush(height_heap, max_height)
        count += 1

if abs(min(height_heap)) < H:
    print('YES')
    print(count)
else:
    print('NO')
    print(abs(heapq.heappop(height_heap)))