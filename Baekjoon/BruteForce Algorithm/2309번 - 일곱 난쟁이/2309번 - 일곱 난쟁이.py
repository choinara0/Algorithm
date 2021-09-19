import sys
from itertools import combinations
height = []
for i in range(9):
    height.append(int(sys.stdin.readline()))

comb = combinations(height, 7)
answer = []
for i in comb:
    if sum(i) == 100:
        answer = sorted(i)
        break

for i in answer:
    print(i)

