import sys
N = int(sys.stdin.readline())
start = []
link = []
matrix = []
minAnswer = float('Inf')

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
def dfs(index):
    global minAnswer
    if index == N // 2:
        startSum = 0
        linkSum = 0
        for i in range(N):
            if i not in start:
                link.append(i)
        for i in range(0, N//2-1):
            for j in range(i+1, N//2):
                startSum += matrix[start[i]][start[j]] + matrix[start[j]][start[i]]
                linkSum += matrix[link[i]][link[j]] + matrix[link[j]][link[i]]

        diff = abs(startSum - linkSum)
        if diff < minAnswer:
            minAnswer = diff
        link.clear()
        return

    for i in range(N):
        if i in start:
            continue
        if len(start) > 0 and start[len(start)-1] > i:
            continue
        start.append(i)
        dfs(index+1)
        start.pop()


dfs(0)
print(minAnswer)