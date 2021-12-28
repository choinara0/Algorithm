import sys

N = int(sys.stdin.readline())
level = [int(sys.stdin.readline().strip()) for i in range(N)]
cnt = 0

for i in range(N-1, 0, -1):
    if level[i] <= level[i-1]:
        cnt += (level[i-1] - level[i] + 1)
        level[i-1] = level[i] - 1

print(cnt)