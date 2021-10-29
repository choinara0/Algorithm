import sys

X, Y = map(int, sys.stdin.readline().split())
Z = Y * 100 // X
start, end = 1, X
answer = sys.maxsize

while start <= end:
    mid = (start + end) // 2
    currentVictory = (Y + mid) * 100 // (X + mid)

    if currentVictory > Z:
        answer = min(answer, mid)
        end = mid - 1
    else:
        start = mid + 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
