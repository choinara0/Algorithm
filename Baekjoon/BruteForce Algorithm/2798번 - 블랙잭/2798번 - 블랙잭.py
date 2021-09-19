import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
a = combinations(num, 3)
answer = 0
for i in a:
    if sum(i) == M:
        answer = sum(i)
        break
    elif sum(i)<M and sum(i)>answer:
        answer = sum(i)
print(answer)


