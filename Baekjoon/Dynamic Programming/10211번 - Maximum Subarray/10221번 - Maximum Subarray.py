import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = arr[0]
    max_dp = -10000000
    for i in range(1, N):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
        if dp[i] > max_dp:
            max_dp = dp[i]

    print(max_dp)