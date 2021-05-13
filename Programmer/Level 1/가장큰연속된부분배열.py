def solution(nums):
    answer = []
    temp = []
    nums_length = int(len(nums))
    for i in range(0, nums_length):
        temp.append([nums[i]])
    for i in range(0, nums_length):
        for j in range(i+1, nums_length):
            temp.append(nums[i:j+1])
    maxarr = min(temp)
    print(maxarr)
    for i in range(0, len(temp)):
        if sum(maxarr) < sum(temp[i]):
            maxarr = temp[i]
    print(maxarr)
    return sum(maxarr)

solution([-5,1,-3,2,-6,5,4])
'''
문제 설명
문제 개요
정수(integer)들이 들어있는 배열이 주어집니다. 주어딘 배열에서 가장 큰 부분배열의 크기를 구하시오. 
여기서 부분배열이란 주어진 배열 내에서 1개 이상의 연속되어 있는 원소들을 뜻합니다. 
부분배열의 "크기" 는 그 연속된 원소들을 전부 합한 것을 말합니다.

예 1)
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
문제 설명: [4,-1,2,1] 의 합이 6으로 가장 큰 부분배열이다.

'''