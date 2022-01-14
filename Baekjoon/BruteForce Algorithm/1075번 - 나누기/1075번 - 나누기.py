import sys

N = (sys.stdin.readline())
F = int(sys.stdin.readline())
answer = int(N[:-3] + '00')

while True:
    if answer % F == 0:
        break
    answer += 1

print(str(answer)[-2:])