import sys

N = int(sys.stdin.readline())
dp = [0, 1, 0, 1, 1] + [0] * (N-4)
stones = [1, 3, 4]

if N <= 4:
    pass
else:
    for i in range(5, N+1):
        if 0 in [dp[i-1], dp[i-3], dp[i-4]]:
            dp[i] = 1
        else:
            dp[i] = 0

if dp[N] == 1:
    print('SK')
else:
    print('CY')