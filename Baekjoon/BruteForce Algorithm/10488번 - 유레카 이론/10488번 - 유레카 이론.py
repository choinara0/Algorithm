import sys

trinum = [n * (n+1) // 2 for n in range(1, 46)]
answer = [0] * 1001

for i in trinum:
    for j in trinum:
        for k in trinum:
            if i + j + k <= 1000:
                answer[i+j+k] = 1

T = int(sys.stdin.readline())
for t in range(T):
    K = int(sys.stdin.readline())
    print(answer[K])