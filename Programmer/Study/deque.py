#dqueue는 stack과 queue를 합친 자료구조로 가장 자라에 원소를 넣거나 뺄 수 있다.
#append(x), popleft(), clear()
'''
Queue를 List로 이용하지 않는 이유 :
stack에서처럼 list.append(), list.pop(0)을 사용하면 리스트를 큐처럼 이용할 수 있다.
하지만 pop()의 time complexity O(1)인 반면, pop(0)의 time complexity는 O(N)이기 떄문.
'''

from collections import deque
#선언
deque1 = deque()
deque2 = deque([1, 2, 3])
deque3 = deque(maxlen=5)

#popleft()
while deque2:
    print("{}를 pop했습니다. ".format(deque2.popleft()))
