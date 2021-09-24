import sys
from itertools import permutations

N = int(sys.stdin.readline())
matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

perm = permutations([i for i in range(N)])
answer = 987654321

def sum_route(r):
    global matrix, N
    tmp = 0
    for i in range(len(r)-1):
        if matrix[r[i]][r[i+1]] == 0:
            return -1
        else:
            tmp += matrix[r[i]][r[i + 1]]

    if matrix[r[-1]][r[0]] == 0:
        return -1
    else:
        tmp += matrix[r[-1]][r[0]]

    return tmp

for i in perm:
    temp = sum_route(i)
    if temp != -1:
        if answer > temp:
            answer = temp

print(answer)

