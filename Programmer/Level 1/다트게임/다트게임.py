
def solution(dartResult):
    answer = []
    a = []
    for i in range(len(dartResult)):
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            a.append('10')
        elif dartResult[i] == '0' and dartResult[i-1] == '1':
            continue
        else:
            a.append(dartResult[i])
    for i in range(1, len(a)):

        if a[i] == 'S':
            answer.append(int(a[i-1]))
        elif a[i] == 'D':
            answer.append(int(a[i-1])**2)
        elif a[i] =='T':
            answer.append(int(a[i-1])**3)
        elif a[i] == '*':
            if len(answer)>=2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif a[i] == '#':
            answer[-1] = answer[-1] * (-1)

    return sum(answer)
solution("10S#10S#10S*")

