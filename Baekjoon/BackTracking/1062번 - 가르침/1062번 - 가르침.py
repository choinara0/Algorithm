import sys

N, K = map(int, sys.stdin.readline().split())
K -= 5
wordList = []
northRule = ['a', 'n', 't', 'i', 'c']
for i in range(N):
    wordList.append(sys.stdin.readline()[4:-5])

resCnt = None
kCnt = 0
index = 0
visited = [False] * 26
for i in northRule:
    visited[ord(i)-97] = True

def dfs(index, cnt):
    global resCnt

    if cnt == K:
        readCnt = 0
        for word in wordList:
            for w in word:
                if visited[ord(w) - 97] == False:
                    break
            else:
                readCnt += 1
        resCnt = max(resCnt, readCnt) if resCnt else readCnt
        return

    for i in range(index, 26):
        if visited[i] == False:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False

if K < 0 or K == 21:
    print(0 if K<0 else N)
    exit()

else:
    dfs(0, 0)
print(resCnt)