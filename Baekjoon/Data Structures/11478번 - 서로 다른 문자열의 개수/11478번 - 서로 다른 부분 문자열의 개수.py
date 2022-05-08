import sys

S = sys.stdin.readline().rstrip()
hash = {}
cnt = 0

for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i : j+1]
        if temp not in hash:
            hash[temp] = 1
            cnt += 1

print(cnt)