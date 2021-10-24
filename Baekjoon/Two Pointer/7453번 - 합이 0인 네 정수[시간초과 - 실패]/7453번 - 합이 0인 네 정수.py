import sys
from collections import Counter

N = int(sys.stdin.readline())
tempList = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
A,B,C,D = zip(*tempList)

AB = []
CD = {}
answer = 0

for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD[C[i]+D[j]] = CD.get(C[i]+D[j], 0) + 1

for ab in AB:
    answer += CD.get(-ab, 0)

print(answer)