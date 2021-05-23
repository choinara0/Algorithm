def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        newarray = array[start:end]
        newarray.sort()
        k = newarray[(commands[i][2] - 1)]
        answer.append(k)

    return answer

solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])