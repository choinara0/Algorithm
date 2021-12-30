# math의 factorial 사용
import sys
import math

def combination(n, m):
    return math.factorial(n) // (math.factorial(n-m) * math.factorial(m))

n, m = map(int, sys.stdin.readline().split())
print(combination(n, m))