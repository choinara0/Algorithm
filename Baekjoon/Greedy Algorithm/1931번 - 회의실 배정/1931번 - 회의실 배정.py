import sys
N = int(sys.stdin.readline())
meeting = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
meeting.sort(key = lambda x:(x[1], x[0]))
cnt = 1
endTime = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= endTime:
        cnt += 1
        endTime = meeting[i][1]

print(cnt)