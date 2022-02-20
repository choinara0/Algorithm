import sys

N, K = map(int, sys.stdin.readline().split())

def prime_num(n, k):
    arr = [1] * (n+1)
    cnt = 0
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            if arr[j]:
                cnt += 1
                arr[j] = 0
                if cnt == k:
                    print(j)
                    break
prime_num(N, K)