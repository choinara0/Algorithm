import sys
l = int(sys.stdin.readline())
s = sorted(list(map(int, sys.stdin.readline().split())))
n = int(sys.stdin.readline())

answer = 0
idx = 0
check = True

if n in s:
    print(0)
else:
    for i in range(l - 1):
        if s[i] < n and n < s[i + 1]:
            idx = i
            check = False
            break
    else:
        for i in range(1, s[idx]):
            for j in range(i + 1, s[idx]):
                if i <= n and j >= n:
                    answer += 1
        print(answer)
    if not check:
        for i in range(s[idx] + 1, s[idx + 1]):
            for j in range(i + 1, s[idx + 1]):
                if i <= n and j >= n:
                    answer += 1
        print(answer)