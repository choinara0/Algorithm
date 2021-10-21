import sys

N = int(sys.stdin.readline())
liquidList = sorted(list(map(int, sys.stdin.readline().split())))
answer = float('inf')
answerLeft, answerMid, answerRight = 0,0,0
for i in range(N-2):
    if i<0 and liquidList[i] == liquidList[i-1]:
        continue
    left, right = i+1, N-1

    while left < right:
        temp = liquidList[left] + liquidList[i] + liquidList[right]

        if abs(temp) < abs(answer):
            answer = temp
            answerLeft = i
            answerMid = left
            answerRight = right

            if answer == 0:
                print(liquidList[answerLeft], liquidList[answerMid], liquidList[answerRight])
                sys.exit(0)

        if temp < 0:
            left += 1
        else:
            right -= 1

print(liquidList[answerLeft], liquidList[answerMid], liquidList[answerRight])
