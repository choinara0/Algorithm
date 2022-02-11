import sys
import math
#math 이용
a, b = map(int, sys.stdin.readline().split())
print(math.gcd(a, b))
print(math.lcm(a, b))

# 직접 함수 작성
def _gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def _lcm(x, y):
    return x*y // _gcd(x,y)

print(_gcd(a, b))
print(_lcm(a, b))