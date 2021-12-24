import sys
T = int(sys.stdin.readline())
button = [300, 60, 10]
buttonCnt = [0, 0, 0]
for i in range(3):
    if T == 0:
        break
    if button[i] > T:
        continue
    buttonCnt[i] += T//button[i]
    T %= button[i]
if T != 0:
    print(-1)
else:
    for i in range(3):
        print(buttonCnt[i], end=' ')