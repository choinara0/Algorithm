# BackTracking 사용해서 푼 코드
import sys
N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)
result = []
def dfs(depth, N, M):
    if depth == M:
        for i in range(0, len(result)):
            print(result[i], end=' ')
        print()
        return
    else:
        for i in range(1, N+1):
            if not visited[i]:
                visited[i] = True
                result.append(i)
                dfs(depth + 1, N, M)
                visited[i] = False
                result.pop()
dfs(0, N, M)

# 1 2 3 4 5

# permutations 사용해서 푼 코드
'''
import sys
from itertools import permutations

N, M = map(int ,sys.stdin.readline().split())
num = [i for i in range(1, N+1)]
perm = permutations(num, M)
for i in perm:
    print(' '.join(map(str, i)))

'''
