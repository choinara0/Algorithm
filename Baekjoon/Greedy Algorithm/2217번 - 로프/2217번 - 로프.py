import sys
N = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for i in range(N)]
rope.sort(reverse=True)
for i in range(N):
    rope.append(rope[i] * (i+1))
print(max(rope))