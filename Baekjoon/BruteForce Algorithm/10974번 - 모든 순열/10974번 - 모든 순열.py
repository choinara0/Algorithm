import sys
from itertools import permutations

N = int(sys.stdin.readline())
num = [i for i in range(1, N+1)]

perm = list(permutations(num, N))

for i in perm:
    for j in i:
        print(j, end=" ")
    print()
