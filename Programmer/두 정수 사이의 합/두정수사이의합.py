def solution(a, b):
    answer = 0
    max = a
    min = b
    if b > a:
        max, min = b, a
    for i in range(min, max + 1):
        answer += i

    return answer