import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hash = {}
answer = []

for i in range(N+M):
    name = input().strip()
    if name not in hash:
        hash[name] = 1
    else:
        hash[name] += 1

for k, v in hash.items():
    if v == 2:
        answer.append(k)
answer.sort()
print(len(answer))
print('\n'.join(map(str, answer)))