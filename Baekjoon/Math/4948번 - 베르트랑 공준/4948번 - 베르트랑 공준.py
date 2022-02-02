import sys
import math

def get_prime(n):
    arr = [1] * (n+1)
    for i in range(2, int(math.sqrt(n+1))+1):
        if arr[i]:
            for j in range(2*i, n+1, i):
                arr[j] = 0

    return arr

primenum_list = get_prime(246912)
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if primenum_list[i]:
            cnt += 1

    print(cnt)