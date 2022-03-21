import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    card_list = deque(list(map(str, sys.stdin.readline().split())))
    answer = str(card_list.popleft())
    while card_list:
        card = card_list.popleft()
        if ord(card) <= ord(answer[0]):
            answer = card + answer
        else:
            answer = answer + card

    print(answer)