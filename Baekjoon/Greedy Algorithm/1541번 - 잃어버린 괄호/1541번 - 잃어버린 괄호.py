import sys
arr = sys.stdin.readline().split('-')
print(arr)
answer = 0
for i in arr[0].split('+'):
    answer += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)
