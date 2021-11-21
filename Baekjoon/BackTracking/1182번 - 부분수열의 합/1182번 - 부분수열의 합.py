import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(1, len(num)+1):
    temp = list(combinations(num, i))
    for j in range(len(temp)):
        if sum(temp[j]) == S:
            answer += 1

print(answer)