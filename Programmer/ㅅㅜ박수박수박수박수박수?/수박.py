def solution(n):
    answer = ''
    temp = '수박'
    for i in range(0, n):
        if i<2:
            answer += temp[i]
        elif i>=2:
            temp_index = int(i%2)
            answer += temp[temp_index]
    print(answer)
    return answer
solution(10)

