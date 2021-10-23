import sys

N = int(sys.stdin.readline())
cardList = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
targetList = list(map(int, sys.stdin.readline().split()))
start, end = 0, len(cardList) - 1

def binarySearch(list, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if list[mid] == target:
            return 1
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for t in targetList:
    print(binarySearch(cardList, t, start, end), end=' ')

