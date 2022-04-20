import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))
sum_value = 0
prefix_sum = [0]

for i in num:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])