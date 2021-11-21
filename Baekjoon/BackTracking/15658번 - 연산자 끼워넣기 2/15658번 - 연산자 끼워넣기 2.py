import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
opList = list(map(int, sys.stdin.readline().split()))
minAns = float('Inf')
maxAns = float('-Inf')
result = 0

def dfs(index, result):
    global minAns
    global maxAns
    if index == N-1:
        if minAns > result:
            minAns = result
        if maxAns < result:
            maxAns = result
        return result
    else:
        for i in range(4):
            temp = result
            if opList[i] == 0:
                continue
            if i == 0:
                result += numList[index+1]
            elif i == 1:
                result -= numList[index+1]
            elif i == 2:
                result *= numList[index+1]
            else:
                if result < 0:
                    result = abs(result) // numList[index + 1] * -1
                else:
                    result //= numList[index+1]
            opList[i] -= 1
            dfs(index+1, result)
            opList[i] += 1
            result = temp

dfs(0, numList[0])
print(maxAns)
print(minAns)