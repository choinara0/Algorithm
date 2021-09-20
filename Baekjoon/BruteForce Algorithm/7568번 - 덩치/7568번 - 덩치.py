import sys
N = int(sys.stdin.readline())
weight = []
height = []
info = [0 for i in range(N)]
for i in range(N):
    w, h= map(int, sys.stdin.readline().split())
    weight.append(w)
    height.append(h)

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        elif height[i]<height[j] and weight[i] < weight[j]:
            info[i] += 1
    info[i] += 1

for i in range(N):
    print(info[i], end=" ")
