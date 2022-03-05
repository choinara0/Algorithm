import heapq

def solution(operations):
    heap = []
    for op in operations:
        o, d = op.split()
        if o == 'I':
            heapq.heappush(heap, int(d))
        elif o == 'D':
            if heap:
                if d == '1':
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                elif d == '-1':
                    heapq.heappop(heap)
    if heap:
        answer = [heapq.nlargest(1, heap)[0], heap[0]]
    else:
        answer = [0, 0]
    return answer

solution(["I 16","D 1"]) # [0,0]
solution(["I 7","I 5","I -5","D -1"]) #[7,5]