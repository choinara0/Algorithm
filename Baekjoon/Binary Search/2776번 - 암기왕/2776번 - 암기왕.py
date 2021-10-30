import sys
T = int(sys.stdin.readline())

def binarySearch(start, end, num):
    global note1
    while start <= end:
        mid = (start + end) // 2
        if note1[mid] == num:
            return 1
        elif note1[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for t in range(T):
    N = int(sys.stdin.readline())
    note1 = sorted(list(map(int, sys.stdin.readline().split())))
    M = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))
    for num in note2:
        print(binarySearch(0, N-1, num))
