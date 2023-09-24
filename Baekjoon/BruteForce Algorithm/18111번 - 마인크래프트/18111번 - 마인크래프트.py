import sys

N, M, B = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = sys.maxsize
floor = 0

for i in range(257):

    append_floor, minus_floor = 0, 0

    for j in range(N):
        for k in range(M):
            if board[j][k] > i:
                minus_floor += board[j][k] - i
            else:
                append_floor += i - board[j][k]

    if minus_floor + B >= append_floor:
        if append_floor + (minus_floor * 2) <= answer:
            answer = append_floor + (minus_floor * 2)
            floor = i

print(answer, floor)