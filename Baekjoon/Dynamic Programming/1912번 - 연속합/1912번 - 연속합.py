import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = num

for i in range(1, N):
    dp[i] = max(num[i], num[i]+dp[i-1])
print(max(dp))