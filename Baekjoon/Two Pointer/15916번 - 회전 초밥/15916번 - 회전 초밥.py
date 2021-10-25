import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().split())
sushiArr = [int(sys.stdin.readline())for i in range(N)]
intDict = defaultdict(int)
intDict[c] = 1
cnt = 1

for i in range(k):
    if intDict[sushiArr[i]] == 0:
        cnt += 1
    intDict[sushiArr[i]] += 1

answer = cnt
for start in range(N):
    end = (start + k) % N
    intDict[sushiArr[start]] -= 1
    if intDict[sushiArr[start]] == 0 :
        cnt -= 1
    if intDict[sushiArr[end]] == 0:
        cnt += 1
    intDict[sushiArr[end]] += 1

    answer = max(answer, cnt)

print(answer)