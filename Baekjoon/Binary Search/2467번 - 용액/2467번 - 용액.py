import sys

N = int(sys.stdin.readline())
liquidList = list(map(int, sys.stdin.readline().split()))
left = 0
right = len(liquidList) - 1
answer = liquidList[left] + liquidList[right]
answerLeft = left
answerRight = right

while left < right :

    temp = liquidList[left] + liquidList[right]

    if abs(temp) < abs(answer):
        answer = temp
        answerLeft = left
        answerRight = right

        if answer == 0:
            break

    if temp < 0 :
        left += 1
    else:
        right -= 1

print(liquidList[answerLeft], liquidList[answerRight])