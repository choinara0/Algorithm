import sys

mush = [int(sys.stdin.readline()) for i in range(10)]
ans, score = 0, 0

for i in range(len(mush)):
    ans = score
    score += mush[i]
    if score == 100:
        print(100)
        sys.exit()

    if score > 100:
        if abs(100 - score) > abs(100 - ans):
            score = ans
        break
print(score)