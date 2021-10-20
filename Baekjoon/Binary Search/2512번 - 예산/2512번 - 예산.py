import sys

N = int(sys.stdin.readline())
requestList = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
start, end = 1, max(requestList)

def binarySearch(list, M, start, end):

    while start <= end:
        mid = (start + end) // 2
        n = 0

        for r in requestList:
            if r >= mid:
                n += mid
            else:
                n += r

        if n <= M:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(binarySearch(requestList, M, start, end))
