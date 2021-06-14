def solution(s):
    answer = ''
    new_answer = sorted(s, reverse=1)
    for i in new_answer:
        answer += i
    return answer