import sys
import heapq
T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    visited = [False] * 1000001
    minH, maxH = [], []
    for j in range(N):
        op= list(sys.stdin.readline().split())

        if op[0] == 'I':
            heapq.heappush(minH, (int(op[1]), j))
            heapq.heappush(maxH, (-1 * int(op[1]), j))
            visited[j] = True

        elif op[0] == 'D':
            if op[1] == '1':
                while maxH and not visited[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    visited[maxH[0][1]] = False
                    heapq.heappop(maxH)
            elif op[1] == '-1':
                while minH and not visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]] = False
                    heapq.heappop(minH)

    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)

    if maxH and minH:
        print(-1 * maxH[0][0], minH[0][0])
    else:
        print('EMPTY')
