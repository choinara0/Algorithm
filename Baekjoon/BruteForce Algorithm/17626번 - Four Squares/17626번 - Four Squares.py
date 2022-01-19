import sys
import math

def solution(n):

    if int(sqrt) == n**0.5:
        return 1

    for i in range(1, int(sqrt) + 1):
        if int((n - i**2)**0.5) == (n - i**2)**0.5:
            return 2

    for i in range(1, int(sqrt) + 1):
        for j in range(1, int((n - i**2)**0.5) + 1):
            if int((n - i**2 - j**2)**0.5) == (n - i**2 - j**2)**0.5:
                return 3

    return 4

n = int(sys.stdin.readline())
sqrt = math.sqrt(n)
print(solution(n))