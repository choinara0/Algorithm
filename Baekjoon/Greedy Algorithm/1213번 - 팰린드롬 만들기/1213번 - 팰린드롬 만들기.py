import sys

name = list(map(str, sys.stdin.readline().strip()))
answer = ''
temp = ''
nameCnt = [0 for i in range(26)]
oddCnt = 0

for i in name:
    nameCnt[ord(i)-65] += 1

for i in range(26):
    if nameCnt[i] % 2 == 1:
        oddCnt += 1
        temp = chr(i+65)
    answer += chr(i+65) * (nameCnt[i] // 2)

reverse_answer = list(answer)
reverse_answer.reverse()

if oddCnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer + temp + ''.join(map(str, reverse_answer)))