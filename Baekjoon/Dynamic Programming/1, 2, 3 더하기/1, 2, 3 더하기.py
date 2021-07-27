import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue
    elif n>3:
        dp = [[0] for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, len(dp)):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[-1])

