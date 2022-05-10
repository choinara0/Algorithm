import heapq

def solution(n, works):
    answer = 0
    heap = []

    if n > sum(works):
        return answer

    for work in works:
        heapq.heappush(heap, [-work, work])

    while n > 0:
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, [-work, work])
        n -= 1

    for work in heap:
        if work[1] < 0:
            continue
        answer += work[1] ** 2

    return answer

solution(4, [4, 3, 3]) #12
solution(1, [2, 1, 2]) #6
solution(3, [1,1]) #0