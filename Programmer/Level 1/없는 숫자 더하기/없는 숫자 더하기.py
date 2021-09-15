def solution(numbers):
    answer = 0
    number = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    inputNum = set(numbers)
    answer = sum(number - inputNum)


    return answer

solution([1,2,3,4,6,7,8,0])
solution([5,8,4,0,6,7,9])