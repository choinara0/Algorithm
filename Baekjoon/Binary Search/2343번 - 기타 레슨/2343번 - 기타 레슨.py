import sys

N, M = map(int, sys.stdin.readline().split())
lesson = list(map(int, sys.stdin.readline().split()))
start, end = sum(lesson)//M, sum(lesson)
answer = end

while start <= end:
    mid = (start + end) // 2
    if mid < max(lesson):
        start = mid + 1
        continue
    cnt, temp = 0,0

    for i in range(len(lesson)):
        if lesson[i] > mid:
            break
        elif temp + lesson[i] <= mid:
            temp += lesson[i]
        else:
            temp = lesson[i]
            cnt += 1

    if cnt <= M - 1:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)