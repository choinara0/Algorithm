import sys

D, K = map(int, sys.stdin.readline().split())
a = K // 2
b = K - a

while True:
    dp = [0] * (D+1)
    dp[D] = K
    dp[D-1] = b
    dp[D-2] = a
    check = False

    for i in range(len(dp)-4, 0, -1):
        temp = dp[i+2] - dp[i+1]
        if temp > dp[i+1]:
            check = True
            break
        else:
            dp[i] = temp
    a -= 1
    b += 1
    if not check:
        break

print(dp[1])
print(dp[2])
