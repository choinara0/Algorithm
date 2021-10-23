import sys

N = int(sys.stdin.readline())
numList = sorted(list(map(int, sys.stdin.readline().split())))
X = int(sys.stdin.readline())
start, end = 0, len(numList) - 1
answer = 0

while(start<end):
    temp = numList[start] + numList[end]

    if temp == X:
        answer += 1
    elif temp < X:
        start += 1
        continue
    end -= 1
print(answer)
