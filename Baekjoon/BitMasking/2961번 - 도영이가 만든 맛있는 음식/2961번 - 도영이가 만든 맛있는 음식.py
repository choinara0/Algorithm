import sys
N = int(sys.stdin.readline())
food = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
minTaste = 1000000000
for i in range(1, 1<<N):
    tasteS = 1
    tasteB = 0
    for j in range(N):
        if i & (1<<j):
            tasteS *= food[j][0]
            tasteB += food[j][1]
            taste = abs(tasteS - tasteB)
            if minTaste > taste:
                minTaste = taste
print(minTaste)

