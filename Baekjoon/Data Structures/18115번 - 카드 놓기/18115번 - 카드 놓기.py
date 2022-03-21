import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
card_list = deque([i for i in range(1, N+1)])
answer = deque()

while A:
    op = A.pop()
    card = card_list.popleft()
    if op == 1:
        answer.appendleft(card)
    elif op == 2:
        answer.insert(1, card)
    elif op == 3:
        answer.append(card)

print(' '.join(map(str, answer)))