import sys

N = int(sys.stdin.readline())
solList = sorted(list(map(int, sys.stdin.readline().split())))
start, end = 0, len(solList)-1
answer = solList[start] + solList[end]
answerLeft = start
answerRight = end

while start < end:

    temp = solList[start] + solList[end]

    if abs(temp) < abs(answer):
        answer = temp
        answerLeft = start
        answerRight = end

        if answer == 0:
            break

    if temp < 0:
        start += 1
    else:
        end -= 1

print(solList[answerLeft], solList[answerRight])