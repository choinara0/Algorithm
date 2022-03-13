import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().strip()[1:-1].split(","))
    check = False
    R_cnt = 0
    if arr[0] == '':
        arr = deque()

    for i in p:
        if i == 'R':
            R_cnt += 1
        if i == 'D':
            if not arr:
                print("error")
                check = True
                break
            if R_cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    if R_cnt % 2 != 0:
        arr.reverse()

    if not check:
        print('[' + ",".join(arr) + "]")