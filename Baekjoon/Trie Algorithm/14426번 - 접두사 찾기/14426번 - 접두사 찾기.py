import sys

N, M = map(int, sys.stdin.readline().split())
string = sorted([sys.stdin.readline().strip() for i in range(N)])
inputString = sorted([sys.stdin.readline().strip() for i in range(M)])
idx = 0
cnt = 0
for i in range(M):
    for j in range(idx, len(string)):
        if string[j].startswith(inputString[i]):
            cnt += 1
            idx = j
            break
print(cnt)