def solution(scores):
    answer = ''

    for i in range(len(scores)):
        temp = []
        for j in range(len(scores[i])):
            temp.append(scores[j][i])
        if (temp[i] == min(temp) or temp[i] == max(temp)) and temp.count(temp[i]) == 1:
            del temp[i]
        mean = sum(temp) / len(temp)
        if mean >= 90: answer += 'A'
        elif mean >= 80: answer += 'B'
        elif mean >= 70: answer += 'C'
        elif mean >= 50: answer += 'D'
        else: answer += 'F'


    return answer

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]) #"FBABD"

solution([[50,90],[50,87]]) #"DA"
solution([[70,49,90],[68,50,38],[73,31,100]]) #"CFD"