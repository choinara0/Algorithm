import sys

N = int(sys.stdin.readline())
inequalitySign = list(map(str, sys.stdin.readline().split()))
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
visited = [False] * (10)
result = []
resultList = []

def dfs():
    if len(result) == N+1:
        resultList.append(''.join(map(str, result)))
        return
    else:
        for i in range(len(num)):
            if visited[i] == False:
                if len(result) == 0:
                    visited[i] = True
                    result.append(num[i])
                    dfs()
                    result.pop()
                    visited[i] = False
                elif inequalitySign[len(result)-1] == '<' and result[-1] < num[i]:
                    visited[i] = True
                    result.append(num[i])
                    dfs()
                    result.pop()
                    visited[i] = False
                elif inequalitySign[len(result)-1] == '>' and result[-1] > num[i]:
                    visited[i] = True
                    result.append(num[i])
                    dfs()
                    result.pop()
                    visited[i] = False


dfs()
print(resultList[-1])
print(resultList[0])




