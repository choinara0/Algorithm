import sys

N, M = map(int, sys.stdin.readline().split())
numList = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]
maxSize = 0
if N > M:
    maxSize = M
else:
    maxSize = N

for i in range(maxSize, 0, -1):
    for j in range(N-i+1):
        for k in range(M-i+1):
            if numList[j][k] == numList[j][k+i-1] == numList[j+i-1][k] == numList[j+i-1][k+i-1]:
                print(i**2)
                sys.exit()