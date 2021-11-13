import sys
N, M = map(int, sys.stdin.readline().split())
dayCost = [int(sys.stdin.readline()) for i in range(N)]
start, end = min(dayCost), sum(dayCost)
answer = 0
while start <= end:
    mid = (start + end ) // 2
    charge = mid
    count = 1
    for i in range(len(dayCost)):
        if charge < dayCost[i]:
            charge = mid
            count += 1
        charge -= dayCost[i]
        if count > M or mid < max(dayCost):
            start = mid + 1
        else:
            end = mid - 1
            answer = mid

print(answer)