import sys

N, S = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
start, end = 0, 0
answer = float('inf')
startSum = numList[0]

if numList[0] >= S:
    print(1)
    sys.exit()


while True:

    if startSum >= S:
        answer = min(answer, end - start + 1)
        startSum -= numList[start]
        start += 1
    else:
        end += 1
        if end == N:
            break
        startSum += numList[end]

if answer == float('inf'):
    print(0)
else:
    print(answer)