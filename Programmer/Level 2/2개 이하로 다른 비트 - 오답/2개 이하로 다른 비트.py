def func_numbers(n):
    bin_num = list('0' + bin(n)[2:])
    idx = ''.join(bin_num).rfind('0')

    if n%2==0:
        bin_num[idx] = '1'
    else:
        bin_num[idx] = '1'
        bin_num[idx+1] = '0'

    return ''.join(bin_num)

def solution(numbers):
    answer = []
    for i in numbers:
        x = func_numbers(i)
        answer.append(int(x,2))

    return answer


solution([2, 7]) #[3,11]

