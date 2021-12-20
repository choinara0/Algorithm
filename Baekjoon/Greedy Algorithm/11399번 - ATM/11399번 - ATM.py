import sys

N = int(sys.stdin.readline())
P = sorted(list(map(int, sys.stdin.readline().split())))
time = P[0]

for i in range(1, len(P)):
    for j in range(i+1):
        time += P[j]

print(time)