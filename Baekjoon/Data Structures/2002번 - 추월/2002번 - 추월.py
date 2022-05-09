import sys
input = sys.stdin.readline

N = int(input())
inside = {}
outside = []
answer = 0

for i in range(N):
    inside[input().rstrip()] = i
for _ in range(N):
    outside.append(input().rstrip())

for i in range(N-1):
    for j in range(i+1, N):
        if inside[outside[i]] > inside[outside[j]]:
            answer += 1
            break

print(answer)