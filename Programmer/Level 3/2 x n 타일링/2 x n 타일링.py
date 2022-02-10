def solution(n):
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, (n+1)):
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
        answer = dp[n]
    return answer

solution(4) #5