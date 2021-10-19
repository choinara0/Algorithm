import sys

K, N = map(int, sys.stdin.readline().split())
lenList = []
for i in range(K):
    lenList.append(int(sys.stdin.readline()))
start, end = 1, max(lenList)

def binarySearch(list, target, start, end):

    while start<=end:
        mid = (start + end) // 2
        lineSum = 0
        for i in list:
            lineSum += i // mid

        if lineSum >= target:
            start = mid + 1
        else:
            end = mid -1

    return end

print(binarySearch(lenList, N, start, end))