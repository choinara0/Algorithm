
#n=진수, t= 미리 구해야 할 숫자의 수, m=참여하는 인원의 수, p=튜브의 순서
def solution(n, t, m, p):
    answer = ''
    alpha = 'ABCDEF'
    length = m * t
    candidate = ''

    for i in range(length +1):
        num = i
        res = ''
        if num == 0:
            candidate += '0'
        else:
            while num > 0:
                if num % n >= 10:
                    res += alpha[(num % n) % 10]
                else:
                    res += str(num % n)
                num = num // n

            candidate += res[::-1]



    for i in range(p-1, len(candidate), m):
        if len(answer) == t:
            break
        else:
            answer += candidate[i]

    return answer


solution(2, 4, 2, 1) # "0111"
solution(16, 16, 2, 1) # "02468ACE11111111"
solution(16, 16, 2, 2) # "13579BDF01234567"
