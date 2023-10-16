import sys

k, s, N = sys.stdin.readline().split()
N = int(N)
king = list(map(int, [ord(k[0])-64, k[1]]))
stone = list(map(int, [ord(s[0])-64, s[1]]))
move = {'R': [0, 1], 'L': [0, -1], 'B': [-1, 0], 'T': [1, 0],
        'RT': [1, 1], 'LT': [1, -1], 'RB': [-1, 1], 'LB': [-1, -1]}

for _ in range(N):
    x = sys.stdin.readline().strip()
    kx = king[0] + move[x][1]
    ky = king[1] + move[x][0]
    if 0 < kx <= 8 and 0 < ky <= 8:
        if stone[0] == kx and stone[1] == ky:
            sx = stone[0] + move[x][1]
            sy = stone[1] + move[x][0]
            if 0 < sx <= 8 and 0 < sy <= 8:
                king[0] = kx
                king[1] = ky
                stone[0] = sx
                stone[1] = sy
        else:
            king[0] = kx
            king[1] = ky

print(chr(king[0] + 64) + str(king[1]))
print(chr(stone[0] + 64) + str(stone[1]))