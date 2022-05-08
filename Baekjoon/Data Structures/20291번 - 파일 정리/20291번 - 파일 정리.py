import sys
input = sys.stdin.readline

N = int(input())
hash = {}
for _ in range(N):
    file_name, extension = input().rstrip().split('.')
    if extension in hash:
        hash[extension] += 1
    else:
        hash[extension] = 1

arr = sorted(hash.items(), key=lambda x:x[0])
for i in arr:
    print(i[0], i[1])