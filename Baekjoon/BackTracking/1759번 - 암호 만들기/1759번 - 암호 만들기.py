import sys
L, C = map(int, sys.stdin.readline().split())
letter = sorted(list(map(str, sys.stdin.readline().split())))
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
result = []
visited = [False] * (C)
vowelCnt = 0
consCnt = 0

def dfs(start, vowelCnt, consCnt):
    if len(result) == L:
        if vowelCnt < 1 or consCnt <2:
            return
        print(''.join(map(str, result)))
        return
    else:
        for i in range(start, len(letter)):
            if visited[i] == False:
                if letter[i] in vowels:
                    visited[i] = True
                    result.append(letter[i])
                    dfs(i, vowelCnt+1, consCnt)
                    result.pop()
                    visited[i] = False
                else:
                    visited[i] = True
                    result.append(letter[i])
                    dfs(i, vowelCnt, consCnt+1)
                    result.pop()
                    visited[i] = False

dfs(0, 0, 0)

