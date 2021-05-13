'''
https://programmers.co.kr/learn/courses/30/lessons/77484
로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다. 1

순위	당첨 내용
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6(낙첨)	그 외
로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.

'''

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