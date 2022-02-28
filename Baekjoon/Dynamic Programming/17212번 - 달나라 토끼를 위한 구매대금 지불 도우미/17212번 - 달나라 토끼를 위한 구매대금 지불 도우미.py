import sys

N = int(sys.stdin.readline())
if N == 0:
    print(0)
elif N == 1 or N == 2 or N == 5 or N == 7:
    print(1)
elif N == 3 or N ==4 or N == 6:
    print(2)
else:
    dp = [100001] * (N+1)
    dp[0], dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = 0, 1, 1, 2, 2, 1, 2, 1
    for i in range(8, N+1):
        if i % 7 == 0:
            dp[i] = i // 7
        else:
            dp[i] = min(dp[i-7], dp[i-5], dp[i-2], dp[i-1]) + 1

    print(dp[N])