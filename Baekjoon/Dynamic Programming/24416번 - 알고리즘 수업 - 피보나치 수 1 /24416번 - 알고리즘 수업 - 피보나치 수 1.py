import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())
code_cnt = 0

def fibonacci(x):
    global code_cnt
    dp = [0] * (x+1)
    dp[1] = dp[2] = 1
    for i in range(3, x+1):
        dp[i] = dp[i-1] + dp[i-2]
        code_cnt += 1
    return dp[x]

print(fibonacci(n), code_cnt)