def solution(numbers):
    answer = ''
    str_nums = list(map(str, numbers))
    str_nums.sort(key=lambda x:x*3, reverse=True)
    print(str(int(''.join(str_nums))))
    return answer

solution([6, 10, 2])
solution([3, 30, 34, 5, 9])
