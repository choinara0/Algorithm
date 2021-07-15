# def solution(land):
#     answer = 0
#     i = 0
#     while(i<len(land)-1):
#         prev_value = max(land[i])
#         prev_idx = land[i].index(max(land[i]))
#         next_value = max(land[i+1])
#         next_idx = land[i+1].index(max(land[i+1]))
#         print(prev_idx, next_idx)
#         if prev_idx != next_idx :
#             answer += prev_value
#             i += 1
#         elif prev_idx == next_idx:
#             land[i+1][next_idx] = -1
#
#         if i==len(land)-1:
#             answer += next_value
#     print(answer)
#     return answer

def solution(land):
    answer = 0
    for i in range(len(land)-1):
        max_value = max(land[i])
        max_idx = land[i].index(max(land[i]))
        land[i].pop(max_idx)
        second_max_value = max(land[i])

        for k in range(4):
            if k == max_idx:
                land[i+1][k] += second_max_value
            else:
                land[i+1][k] += max_value
    answer = max(land[-1])
    return answer

solution([[4,3,2,1], [2,2,2,1], [6,6,6,4], [8,7,6,5]])