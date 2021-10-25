import sys

N = int(sys.stdin.readline())
start, end, answer = 0, 1, 1
startSum = 1
while (start < N // 2 + 1):
    if startSum < N:
        end += 1
        startSum += end
    elif startSum > N:
        startSum -= start
        start += 1
    else:
        answer += 1
        end += 1
        startSum -= start
        startSum += end
        start += 1

print(answer)