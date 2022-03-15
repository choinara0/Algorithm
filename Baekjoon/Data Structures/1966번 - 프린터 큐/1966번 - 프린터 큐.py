import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print_list = deque(list(map(int, sys.stdin.readline().split())))
    check_list = [0 for i in range(N)]
    check_list[M] = 1
    check_list = deque(check_list)
    cnt = 0

    while True:

        if print_list[0] == max(print_list):
            cnt += 1

            if check_list[0] == 1:
                print(cnt)
                break
            else:
                print_list.popleft()
                check_list.popleft()

        else:
            print_list.append(print_list.popleft())
            check_list.append(check_list.popleft())