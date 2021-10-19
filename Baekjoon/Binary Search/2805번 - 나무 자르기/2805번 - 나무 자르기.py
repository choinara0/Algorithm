import sys

N, M = map(int, sys.stdin.readline().split())
treeList = sorted(list(map(int, sys.stdin.readline().split())))
start, end = 1, max(treeList)

def binarySearch(list, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        logLength = 0

        for t in list:
            temp = t - mid
            if temp <= 0:
                continue
            else:
                logLength += temp

        if logLength >= target:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(binarySearch(treeList, M, start, end))