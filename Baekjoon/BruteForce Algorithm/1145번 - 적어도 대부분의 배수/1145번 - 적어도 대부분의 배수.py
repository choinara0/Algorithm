import sys
from itertools import combinations
from math import lcm

numList = list(map(int, sys.stdin.readline().split()))
answer = float('Inf')

for comb in combinations(numList, 3):
    a, b, c = map(int, comb)
    if answer > lcm(a, b, c):
        answer = lcm(a, b, c)

print(answer)