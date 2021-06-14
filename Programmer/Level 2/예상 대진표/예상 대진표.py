def solution(n,a,b):
    answer = 0
    # idx_list = [i for i in range(1, n+1)]

    while a!=b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2


    return answer