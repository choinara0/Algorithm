# permuations로 풀기
import sys
from itertools import permutations

X = list(map(str, sys.stdin.readline().strip()))
x = int(''.join(map(str, X)))
result = set()
for comb in permutations(X, len(X)):
    result.add(int(''.join(map(str, comb))))
result = list(result)
result.sort()
for i in range(len(result)):
    if result[i] > x :
        print(result[i])
        sys.exit()
print(0)