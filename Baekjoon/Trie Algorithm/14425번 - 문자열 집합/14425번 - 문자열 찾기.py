import sys

N, M = map(int, sys.stdin.readline().split())
stringSet = list(sys.stdin.readline().strip() for i in range(N))
answer = 0
idx = 0

for i in range(M):
    inputString = sys.stdin.readline().strip()
    if inputString in stringSet:
        answer += 1
print(answer)