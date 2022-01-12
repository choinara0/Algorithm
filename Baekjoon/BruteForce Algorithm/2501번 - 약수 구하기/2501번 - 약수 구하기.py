import sys

N, K = map(int, sys.stdin.readline().split())
answer = []
for i in range(1, N+1):
    if N % i == 0:
        answer.append(i)
        if len(answer) == K:
            print(i)
            break

if len(answer) < K:
    print(0)