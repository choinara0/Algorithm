def solution(n):
    answer = 0
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        answer = dp[n] % 1234567
    return answer


solution(4) # 5
solution(3) # 3