'''import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(1, len(num)+1):
    temp = list(combinations(num, i))
    for j in range(len(temp)):
        if sum(temp[j]) == S:
            answer += 1

print(answer)'''

# 백트래킹으로 풀기

import sys
N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = 0

def dfs(i, graph, result):
    global answer, S
    if result == S:
        answer += 1

    for j in range(i+1, len(num)):
        dfs(j, num, result + num[j])

    return

for i in range(len(num)):
    dfs(i, num, num[i])

print(answer)