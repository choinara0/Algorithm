# math.gcd 사용
import sys
import math

A, B = map(int, sys.stdin.readline().split())
C = math.gcd(A, B)

for _ in range(C):
    print(1, end='')

# 직접 gcd 구현하기

A, B = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if a == b:
        return a
    while b:
        a, b = b, a % b
    return a

C = gcd(A, B)
for _ in range(C):
    print(1, end='')