import sys
from itertools import combinations
from collections import Counter

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
sum_S = []

for i in range(1, N+1):
    for comb in list(combinations(S, i)):
        sum_S.append(sum(comb))
sum_S.sort()

check_num = [i for i in range(1, sum_S[-1]+2)]

answer = Counter(check_num) - Counter(sum_S)
print(list(answer.keys())[0])