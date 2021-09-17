import sys
from itertools import permutations
N = int(sys.stdin.readline())
numData = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = list(permutations(numData, 3))

for i in range(N):
    testCase, strike, ball = map(int, sys.stdin.readline().split())
    testCase = list(str(testCase))
    removed_cnt = 0

    for j in range(len(num)):
        strike_cnt = ball_cnt = 0
        j -= removed_cnt

        for k in range(3):
            testCase[k] = int(testCase[k])
            if testCase[k] in num[j]:
                if k == num[j].index(testCase[k]):
                    strike_cnt += 1
                else:
                    ball_cnt += 1
        if strike_cnt != strike or ball_cnt != ball:
            num.remove(num[j])
            removed_cnt += 1

print(len(num))


