import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
prefix_sum = [0]
sum_value = 0

for i in num:
    sum_value += i
    prefix_sum.append(sum_value)

M = int(input())

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])