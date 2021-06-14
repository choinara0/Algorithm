
'''
위와 같은 방식으로 문제를 풀자 계속 시간 초과가 나왔다. 그래서 heap에 대해 공부를 했다.
*** 항상 오름차순을 정렬을 원할 때는 heqp을 생ㅇ각하자 ***
'''
import heapq
#힙의 특성은 가장 작은 요소가 항상 루트인 heap[0]이다.
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(len(scoville)>1):
        if scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            temp = a + (b*2)
            heapq.heappush(scoville, temp)
            answer += 1
        else:
            break
    for i in scoville:
        if i<K:
            return -1

    return answer

solution([1, 2, 3, 9, 10, 12], 7)