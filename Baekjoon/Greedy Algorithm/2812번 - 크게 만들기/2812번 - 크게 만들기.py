import sys

N, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().strip()))
cnt, stack = K, []

for i in range(N):
    while cnt > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        cnt -= 1
    stack.append(num[i])

print(''.join(map(str, stack[:N-K])))