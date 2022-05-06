import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    arr1 = [int(input()) for _ in range(N)]
    arr2 = [int(input()) for _ in range(M)]
    answer, idx1, idx2 = 0, 0, 0

    while True:
        if arr1[idx1] == arr2[idx2]:
            answer += 1
            idx1 += 1
            idx2 += 1
        elif arr1[idx1] > arr2[idx2]:
            idx2 += 1
        else:
            idx1 += 1

        if idx1 > N-1 or idx2 > M-1:
            break

    print(answer)