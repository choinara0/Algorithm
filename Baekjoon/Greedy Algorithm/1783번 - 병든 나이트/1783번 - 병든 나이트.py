import sys

N, M = map(int, sys.stdin.readline().split())
if N == 1:
    moveCnt = 1
elif N == 2:
    moveCnt = min(4, (M-1)//2 + 1)
elif M < 7:
    moveCnt = min(4, M)
else:
    moveCnt = (2+(M-5)) + 1

print(moveCnt)