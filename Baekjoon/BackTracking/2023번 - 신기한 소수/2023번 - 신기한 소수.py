import sys, math

N = int(sys.stdin.readline())

result = []
start = ['2', '3', '5', '7']
end = ['1', '3', '7', '9']

def isPrime(n):
    number = int(n)
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

def dfs(num):
    if len(num) == N:
        print(num)
        return
    else:
        for i in end:
            if isPrime(num+i):
                dfs(num+i)
for i in start:
    dfs(i)