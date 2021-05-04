def solution(seoul):
    answer = ''
    kim_index = 0
    for i in range(0, len(seoul)):
        if seoul[i] == 'Kim':
            kim_index = i
            break
    answer = "김서방은 {}에 있다".format(kim_index)
    return answer