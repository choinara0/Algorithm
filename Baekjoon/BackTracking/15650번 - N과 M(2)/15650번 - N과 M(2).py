# BackTraking을 이용하여 푼 코드
import sys
N, M = map(int, sys.stdin.readline().split())
result = []
def dfs(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(start, N+1):
            if i not in result:
                result.append(i)
                dfs(i+1)
                result.pop()
    return
dfs(1)

# combinations를 이용해서 푼 코드
'''
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
num = [i for i in range(1, N+1)]
comb = combinations(num, M)
for i in comb:
    print(' '.join(map(str, i)))
'''