import sys

N = int(sys.stdin.readline())
cardList = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
targetList = list(map(int, sys.stdin.readline().split()))
start = 0
end = len(cardList) - 1
cardDict = dict()

for i in cardList:
    if i not in cardDict:
        cardDict[i] = 1
    else:
        cardDict[i] += 1

def binarySearch(list, target, start, end):

    while (start <= end):
        mid = (start + end) // 2

        if list[mid] == target:
            return cardDict[target]
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return 0

for i in targetList:
    print(binarySearch(cardList, i, start, end), end=' ')