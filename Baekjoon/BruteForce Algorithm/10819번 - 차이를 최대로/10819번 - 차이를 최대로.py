import sys
from itertools import permutations

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
maximum = 0
for i in list(permutations(num, N)):
    temp = 0
    for k in range(len(i)-1):
        temp += abs(i[k]-i[k+1])

    if maximum < temp:
        maximum = temp

print(maximum)