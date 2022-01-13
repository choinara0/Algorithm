import sys

N, K, L = map(int, sys.stdin.readline().split())
answer = 0

while K != L:
    K -= K // 2
    L -= L // 2
    answer += 1

print(answer)