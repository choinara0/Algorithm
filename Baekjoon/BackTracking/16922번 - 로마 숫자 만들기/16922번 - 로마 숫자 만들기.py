# combinations_with_replacement로 풀기
import sys
from itertools import combinations_with_replacement

N = int(sys.stdin.readline())
arr = [1, 5, 10, 50]
answer = set()
for comb in combinations_with_replacement(arr, N):
    answer.add(sum(comb))

print(len(answer))

# backtracking으로 풀기
N = int(sys.stdin.readline())
number = [1, 5, 10, 50]
numberList = []
sumList = [0] * 1001

def backtrack(depth, num):
    try:
        if depth == N:
            sumList[sum(numberList)] = 1
            return

        for i in range(num, 4):
            numberList.append(number[i])
            backtrack(depth + 1, i)
            numberList.pop()
    except:
        print(len(sumList))


backtrack(0, 0)
print(sum(sumList))