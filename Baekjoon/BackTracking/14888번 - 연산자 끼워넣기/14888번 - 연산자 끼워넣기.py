import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
result = 0
resultList = []
minAns = float('Inf')
maxAns = float('-Inf')
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
            if op[i] == 0:
                continue
            if i == 0:
                result += num[index+1]
            elif i == 1:
                result -= num[index+1]
            elif i == 2:
                result *= num[index+1]
            else:
                if result < 0:
                    result = abs(result) // num[index + 1] * -1
                else:
                    result //= num[index + 1]

            op[i] -= 1
            dfs(index+1, result)
            op[i] += 1
            result = temp



dfs(0, num[0])
print(maxAns)
print(minAns)
