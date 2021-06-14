
def solution(priorities, location):
    prio_temp = [i for i in range(len(priorities))]
    temp = []
    while(priorities):
        if priorities[0] == max(priorities):
            temp.append(prio_temp.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            prio_temp.append(prio_temp.pop(0))

    return print(temp.index(location) + 1)



solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)