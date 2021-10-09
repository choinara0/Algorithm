import sys
N = int(sys.stdin.readline())
num = []
for i in range(N):
    num.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(len(num[i])):
        if j == 0:
            num[i][j] = num[i-1][j] + num[i][j]
        elif j == len(num[i])-1:
            num[i][j] = num[i-1][j-1] + num[i][j]
        else:
            num[i][j] = max(num[i-1][j-1], num[i-1][j]) + num[i][j]

print(max(num[N-1]))