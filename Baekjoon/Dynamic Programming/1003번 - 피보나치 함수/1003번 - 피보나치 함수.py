import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    zero_cnt = [1, 0]
    one_cnt = [0, 1]

    for i in range(2, N+1):
        zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
        one_cnt.append(one_cnt[i-1] + one_cnt[i-2])

    print("{} {}".format(zero_cnt[N], one_cnt[N]))

'''
def fibonacci(n):
    global zero_cnt
    global one_cnt
    if n==0:
        zero_cnt += 1
    elif n==1 :
        one_cnt += 1
    else:
        fibonacci(n-1)
        fibonacci(n-2)


import sys
T = int(sys.stdin.readline())
sys.setrecursionlimit(10**6)
for i in range(T):
    N = int(sys.stdin.readline())

    zero_cnt = 0
    one_cnt = 0

    fibonacci(N)
    print(zero_cnt, " ", one_cnt)


'''
'''
0 1 1 2 3 5 8 13 21 34 55 ...
'''