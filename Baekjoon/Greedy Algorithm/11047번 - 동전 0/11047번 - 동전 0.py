import sys
N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for i in range(N)]
coinCnt = 0

for i in range(N-1, -1, -1):
    if K == 0:
        break
    if coin[i] > K:
        continue
    coinCnt += K//coin[i]
    K %= coin[i]

print(coinCnt)