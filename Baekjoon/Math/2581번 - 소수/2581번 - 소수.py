import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

def prime_num(a, b):
    arr = [1] *(b+1)
    arr2 = []

    for i in range(2, b+1):
        if arr[i]:
            for j in range(i*i, b+1, i):
                arr[j] = 0
            if i>=a:
                arr2.append(i)

    return arr2

prime_list = prime_num(M, N)
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])