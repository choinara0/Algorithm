import sys
from itertools import combinations

numList = [int(sys.stdin.readline()) for i in range(9)]
sumList = sum(numList) - 100

for comb in combinations(numList, 2):
    if sum(comb) == sumList :
        numList.remove(comb[0])
        numList.remove(comb[1])
        break

print('\n'.join(map(str, numList)))