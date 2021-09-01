def solution(word):
    answer = 0
    vowelDict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    for i, j in enumerate(word):
        temp = 0
        answer += 1
        if j != 'A':
            for k in range(5 - i):
                temp += 5 ** k
            answer += temp * vowelDict[j]
    return answer

solution('AAAAE') #6
solution('AAAE') #10
solution("I") #1563
solution("EIO") #1189