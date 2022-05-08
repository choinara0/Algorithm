import sys

N, C = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
hash = {}

for i in num_list:
    if i not in hash:
        hash[i] = 1
    else:
        hash[i] += 1

arr = sorted(hash.items(), key=lambda x:-x[1])

for i in range(len(arr)):
    for j in range(arr[i][1]):
        print(arr[i][0], end=' ')