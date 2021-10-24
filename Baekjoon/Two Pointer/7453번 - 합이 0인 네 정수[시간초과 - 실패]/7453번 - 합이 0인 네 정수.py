import sys
from collections import Counter

N = int(sys.stdin.readline())
tempList = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(tempList[i][0] + tempList[j][1])
        CD.append(tempList[i][2] + tempList[j][3])
AB.sort()
CD.sort()
answer = 0

print(answer)