import sys
from itertools import permutations

# permutation 사용시 메모리, 시간 초과
N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
perm_list = [list(perm) for perm in permutations([i for i in range(1, N+1)], N)]
check = False
for i in range(len(perm_list)-1):
    if perm_list[i] == p:
        print(' '.join(map(str, perm_list[i+1])))
        check = True
        break

if not check:
    print(-1)

# 다른 방법으로 풀이
N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
point = -1

for i in range(N-1, 0, -1):
    if p[i-1] < p[i]:
        point = i -1
        break
else:
    print(-1)
    sys.exit()

for i in range(N-1, 0, -1):
    if p[point] < p[i]:
        p[point], p[i] = p[i], p[point]
        answer = p[:point+1]+sorted(p[point+1:])
        print(*answer)
        break
