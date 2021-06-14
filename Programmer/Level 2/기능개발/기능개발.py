from collections import deque

def solution(progresses, speeds):
    day = deque()
    deque_prog = deque(progresses)
    cnt = 0
    answer = []
    while(deque_prog):
        cnt += 1
        for i in range(len(speeds)):
            deque_prog[i] +=speeds[i]

        while(deque_prog):
            if deque_prog[0]>= 100:
                deque_prog.popleft()
                speeds.pop(0)
                day.append(cnt)
            else:
                break

    check = 1

    while(day):
        x = day.popleft()
        if not day:
            answer.append(check)
            break
        if x != day[0]:
            answer.append(check)
            check = 1

        elif x == day[0]:

            check += 1


    return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])