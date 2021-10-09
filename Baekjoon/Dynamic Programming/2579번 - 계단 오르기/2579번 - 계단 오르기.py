import sys

N = int(sys.stdin.readline())
stair = []
for i in range(N):
    stair.append(int(sys.stdin.readline()))
if N == 1:
    print(stair[0])
    sys.exit()
elif N == 2:
    print(max(stair[0]+stair[1], stair[1]))
    sys.exit()

dp = [0 for i in range(N)]
dp[0] = stair[0]
dp[1] = max(dp[0] + stair[1], stair[1])
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[N-1])

