import sys
import math
from itertools import combinations

t = int(sys.stdin.readline())
for _ in range(t):
    num = list(map(int, sys.stdin.readline().split()))
    if len(num) == 1:
        print(num[0])
        continue
    else:
        gcd_list = []
        for comb in combinations(num[1:], 2):
            a, b = comb
            gcd_list.append(math.gcd(a, b))
    print(sum(gcd_list))