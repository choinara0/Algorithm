import sys

N = int(sys.stdin.readline())
numList = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
targetList = list(map(int, sys.stdin.readline().split()))
start = 0
end = len(numList) - 1

def binarySearch(list, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if list[mid] == target:
            return 1
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return 0

for i in targetList:
    print(binarySearch(numList, i, start, end))