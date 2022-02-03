import sys

arr = list()
result = set()

def dfs():
    if len(arr) > 0:
        result.add(int(''.join(map(str, arr))))
    for i in range(0, 10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            dfs()
            arr.pop()


N = int(sys.stdin.readline())

try:
    dfs()
    result = list(result)
    result.sort()
    print(result[N-1])

except:
    print(-1)