def solution(lottos, win_nums):
    answer = []
    best_score = 0
    worst_score = 0
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                worst_score += 1
                break
    best_score = worst_score
    for i in range(len(lottos)):
        if lottos[i] == 0:
            best_score += 1

    if best_score == 6:
        answer.append(1)
    elif best_score == 5:
        answer.append(2)
    elif best_score == 4:
        answer.append(3)
    elif best_score == 3:
        answer.append(4)
    elif best_score == 2:
        answer.append(5)
    else:
        answer.append(6)

    if worst_score == 6:
        answer.append(1)
    elif worst_score == 5:
        answer.append(2)
    elif worst_score == 4:
        answer.append(3)
    elif worst_score == 3:
        answer.append(4)
    elif worst_score == 2:
        answer.append(5)
    else:
        answer.append(6)


    return answer

solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])