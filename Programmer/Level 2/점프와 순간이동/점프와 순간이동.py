def solution(n):

    cnt = 0

    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            cnt += 1


    return cnt

solution(5)
solution(6)
solution(5000)