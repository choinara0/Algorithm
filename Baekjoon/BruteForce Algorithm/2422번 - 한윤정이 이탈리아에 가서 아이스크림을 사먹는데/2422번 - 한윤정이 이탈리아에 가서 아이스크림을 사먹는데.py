import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
ice_combination = list(combinations(range(1, N+1), 3))
no_combination = [[0] * (N+1) for i in range(N+1)]
answer = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    no_combination[a][b] = 1
    no_combination[b][a] = 1

for ice_comb in ice_combination:
    if no_combination[ice_comb[0]][ice_comb[1]] or no_combination[ice_comb[0]][ice_comb[2]] or no_combination[ice_comb[1]][ice_comb[2]]:
        continue
    answer += 1

print(answer)