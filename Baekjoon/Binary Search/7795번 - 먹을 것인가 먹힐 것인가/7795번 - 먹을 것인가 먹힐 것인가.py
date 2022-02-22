import sys

def binary_search(target, arr):
    start, end = 0, len(arr) - 1
    result = -1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = sorted(list(map(int, sys.stdin.readline().split())))
    count = 0

    for a in A:
        count += binary_search(a, B) + 1

    print(count)