'''
OO 조선소에서는 태풍으로 인한 작업지연으로 수주한 선박들을 기한 내에 완성하지 못할 것이 예상됩니다.
기한 내에 완성하지 못하면 손해 배상을 해야 하므로 남은 일의 작업량을 숫자로 매기고 배상비용을 최소화하는 방법을 찾으려고 합니다.
배상 비용은 각 선박의 완성까지 남은 일의 작업량을 제곱하여 모두 더한 값이 됩니다.

조선소에서는 1시간 동안 남은 일 중 하나를 골라 작업량 1만큼 처리할 수 있습니다.
조선소에서 작업할 수 있는 N 시간과 각 일에 대한 작업량이 담긴 배열(works)이 있을 때 배상 비용을 최소화한 결과를 반환하는 함수를 만들어 주세요.
예를 들어, N=4일 때, 선박별로 남은 일의 작업량이 works = [4, 3, 3]이라면
배상 비용을 최소화하기 위해 일을 한 결과는 [2, 2, 2]가 되고 배상 비용은 2**2 + 2**2 + 2**2 = 12가 되어 12를 반환해 줍니다.

제한사항
일할 수 있는 시간 N : 1,000,000 이하의 자연수
배열 works의 크기 : 1,000 이하의 자연수
각 일에 대한 작업량 : 1,000 이하의 자연수
입출력 예
N	works	result
4	[4,3,3]	12
2	[3,3,3]	17

'''

'''
처음 짠 효율성 실패 코드

def solution(no, works):
    result = 0
    if no >= sum(works):
        return 0
    for i in range(no):
        works[works.index(max(works))] = works[works.index(max(works))] -1

    for i in range(len(works)):
        result += works[i]**2
    return result
'''

import heapq
def solution(no, works):
    if no>= sum(works):
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    for i in range(no):
        max_w = heapq.heappop(works)
        heapq.heappush(works, max_w+1)
    return sum([i**2 for i in works])
solution(4, [4,3,3])
solution(2, [3,3,3])