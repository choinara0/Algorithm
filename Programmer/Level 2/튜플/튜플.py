def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    for i in s:
        new_i = i.split(',')
        for j in new_i:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")