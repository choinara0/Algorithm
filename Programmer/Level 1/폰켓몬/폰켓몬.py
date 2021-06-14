def solution(nums):
    answer = 0
    get_n = []
    get_n.append(nums[0])
    for i in range(1, len(nums)):
        if 2*len(get_n) == len(nums):
            break
        if nums[i] not in get_n :
            get_n.append(nums[i])
            print(i, get_n)
    answer = len(get_n)
    print(answer)
    return answer
'''
3, 1, 2, 3
3, 1
'''
solution([3,1,2,3])