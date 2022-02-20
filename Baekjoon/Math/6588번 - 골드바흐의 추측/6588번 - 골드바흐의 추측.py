import sys
import math

arr = [1] * 1000000
for i in range(2, int(math.sqrt(1000000))+1):
    if arr[i]:
        for j in range(i*i, 1000000, i):
            arr[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, 1000000):
        if arr[i] and arr[n-i]:
            print("%d = %d + %d" %(n, i, n-i))
            break