def solution(answers):
    answer = []
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    for i in range(len(answers)):
        if student_1[i % len(student_1)] == answers[i]:
            cnt_1 += 1
        if student_2[i % len(student_2)] == answers[i]:
            cnt_2 += 1
        if student_3[i % len(student_3)] == answers[i]:
            cnt_3 += 1
    max_score = max(cnt_1, cnt_2, cnt_3)
    if max_score == cnt_1:
        answer.append(1)
    if max_score == cnt_2:
        answer.append(2)
    if max_score == cnt_3:
        answer.append(3)

    return answer