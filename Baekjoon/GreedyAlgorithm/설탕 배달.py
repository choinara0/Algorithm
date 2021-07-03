import sys
N = int(sys.stdin.readline())
cnt = 0
while(1):
    if N % 5 == 0:
        cnt = cnt + (N//5)
        print(cnt)
        break
    else:
        cnt += 1
        N -= 3

    if N < 0:
        print(-1)
        break

