import sys

R, C, W = map(int, sys.stdin.readline().split())
dp = [[1] * i for i in range(31)]
answer = 0
cnt = 1

for i in range(3, 31):
    for j in range(1, i-1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for i in range(R, R+W):
    for j in range(cnt):
        answer += dp[i][C-1+j]
    cnt += 1

print(answer)