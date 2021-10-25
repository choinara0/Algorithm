import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ingreList = sorted(list(map(int , sys.stdin.readline().split())))
answer, start, end = 0, 0, N-1

while(start < end):
    tempSum = ingreList[start] + ingreList[end]

    if tempSum == M:
        answer += 1
        start += 1
        end -= 1
    elif tempSum < M:
        start += 1
    else:
        end -= 1

print(answer)
