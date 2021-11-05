import sys
sys.setrecursionlimit(10**6)
nodeList = []

def dfs(arr):
    if len(arr) == 1:
        print(arr[0])
        return
    if len(arr) < 1:
        return

    root = arr[0]
    mid = len(arr)

    for i in range(1, len(arr)):
        if arr[i] > root:
            mid = i
            break
    dfs(arr[1:mid])
    dfs(arr[mid:])
    print(root)

while True:
    try:
        nodeList.append(int(input()))
    except:
        break

dfs(nodeList)
