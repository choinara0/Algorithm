import sys
import math

def get_primenum(n, m):
    arr = [1] * (m+1)
    for i in range(2, int(math.sqrt(m+1)) + 1):
        if arr[i] == True:
            for j in range(2*i, m+1, i):
                arr[j] = 0
    return arr


N, M = map(int, sys.stdin.readline().split())
primenum_list = get_primenum(N, M)

for i in range(N, M+1):
    if i > 1 and primenum_list[i]:
        print(i)