import sys


N = int(sys.stdin.readline())
sieve = [True] * (N+1)
M = int((N+1)**0.5)

for i in range(2, M + 1):
    if sieve[i] == True:
        for j in range(i+i, N+1, i):
            sieve[j] = False

primeList = [i for i, j in enumerate(sieve) if j == True and i>=2]
answer, start, end = 0, 0, 0

while end <= len(primeList):
    tempSum = sum(primeList[start:end])
    if tempSum == N:
        answer += 1
        end += 1
    elif tempSum<= N:
        end += 1
    else:
        start += 1
print(answer)