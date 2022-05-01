import sys
from copy import deepcopy
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
prefix_sum = deepcopy(arr)

for i in range(1, N):
    prefix_sum[i] += prefix_sum[i-1]

for k in range(1, N-1):
    answer = max(answer, 2*prefix_sum[-1] - arr[0] - arr[k] - prefix_sum[k])

for k in range(1, N-1):
    answer = max(answer, prefix_sum[-1] - arr[-1] - arr[k] + prefix_sum[k-1])

for k in range(1, N-1):
    answer = max(answer, prefix_sum[k] - arr[0] + prefix_sum[-1] - prefix_sum[k-1] - arr[-1])

print(answer)