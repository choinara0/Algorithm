import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().split())
sushiArr = [int(sys.stdin.readline().rstrip()) for i in range(N)]
left, right, answer = 0, 0, 0
sushiArr.extend(sushiArr)
intDict = defaultdict(int)
intDict[c] += 1
while right < k:
    intDict[sushiArr[right]] += 1
    right += 1


while right < len(sushiArr):
    answer = max(answer, len(intDict))
    intDict[sushiArr[left]] -= 1
    if intDict[sushiArr[left]] == 0:
        del intDict[sushiArr[left]]
    intDict[sushiArr[right]] += 1
    left += 1
    right += 1

print(answer)