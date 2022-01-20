import sys
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
answer = 0

for i in range(N, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1] and is_prime(i):
        answer = i
        break

if answer == 0:
    answer = 1003001

print(answer)