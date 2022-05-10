def adj(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def findQueen(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if adj(x):
                findQueen(x+1)
    return

N = int(input())
row = [0] * N
result = 0
findQueen(0)
print(result)


