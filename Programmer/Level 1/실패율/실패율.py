
def solution(N, stages):
    # answer = []
    # arrive = [0 for i in range(N+1)]
    # clear = [-3 for i in range(N+1)]
    # for i in stages:
    #     cnt = i-1
    #     while(cnt>=0):
    #         arrive[cnt] += 1
    #         cnt -=1
    # print(arrive)
    #
    # for i in range(N):
    #     if arrive[i] == arrive[i+1] and i+1==N:
    #         clear[i] = -1
    #     else:
    #         clear[i] = (arrive[i] - arrive[i+1]) / arrive[i]
    # print(clear)
    #
    # for i in range(len(clear)-1):
    #     answer.append(clear.index(max(clear))+1)
    #     clear[clear.index(max(clear))] = -2
    #
    # print(answer)
    s = []
    k = len(stages)
    for i in range(1, N+1):
        c = 0
        for j in range(len(stages)):
            if stages[j] == i:
                c += 1
        if c==0:
            s.append(0)
        else:
            s.append(c/k)
        k = k -c
        print(s)
    a = sorted(s, reverse=1)
    answer = []
    for i in range(len(a)):
        answer.append(s.index(a[i])+1)
        s[s.index(a[i])] = 2
    print(answer)
    return answer
solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
'''
1/8, 3/7, 2/4,  1/2, 0/1
'''

