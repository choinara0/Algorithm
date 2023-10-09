import sys

N = int(sys.stdin.readline())
t = [0] * N
p = [0] * N

for _ in range(N):
    t[_], p[_] = map(int, sys.stdin.readline().split())


dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if t[i] + i > N: # t[i] + i 가 퇴사일을 넘어간다면 그 전날 값을 가져옴
        dp[i] = dp[i+1]
    else: #상담을 안했을 때(dp[i+1])와 상담을 했을 떄(dp[i+t[i]] + p[i])의 수익을 비교
        dp[i] = max(dp[i+1] , dp[i+t[i]] + p[i])

print(dp[0])