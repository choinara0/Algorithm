import sys
input = sys.stdin.readline

N = int(input())
hash = {}

for _ in range(N):
    card = int(input())
    if card not in hash:
        hash[card] = 1
    else:
        hash[card] += 1

arr = sorted(hash.items(), key=lambda x:(-x[1], x[0]))
print(arr[0][0])