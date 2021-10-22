import sys

N, K = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
answer = float('-inf')
sumArr = 0
start = 0
for end in range(N):
    sumArr += numList[end]
    if end - start + 1 == K:
        answer = max(answer, sumArr)
        sumArr -= numList[start]
        start += 1
print(answer)
