import sys

prime_num = [0, 0, 1] + [1] * 10000
for i in range(2, 10000):
    if prime_num[i]:
        for j in range(i*2, 10000, i):
            prime_num[j] = 0

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    start = n // 2
    end = start

    while start > 0:
        if prime_num[start] and prime_num[end]:
            print(start, end)
            break
        else:
            start -= 1
            end += 1