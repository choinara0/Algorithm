def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [1, 0], 3: [2,0], 4:[0, 1], 5:[1, 1], 6:[2,1], 7:[0,2], 8:[1,2], 9:[2,2], 0:[1, 3]}
    current_left = [0,3]
    current_right = [2,3]
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            current_left = keypad[numbers[i]]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            current_right = keypad[numbers[i]]
        else:
            right_temp = abs(keypad[numbers[i]][0] - current_right[0]) + abs(keypad[numbers[i]][1] - current_right[1])
            left_temp = abs(keypad[numbers[i]][0] - current_left[0]) + abs(keypad[numbers[i]][1] - current_left[1])
            if right_temp == left_temp:
                if hand == 'right':
                    answer += 'R'
                    current_right = keypad[numbers[i]]
                else:
                    answer += 'L'
                    current_left = keypad[numbers[i]]
            elif right_temp > left_temp:
                answer += 'L'
                current_left = keypad[numbers[i]]
            else:
                answer += 'R'
                current_right = keypad[numbers[i]]
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left')
# keypad = {1: [0, 0], 2: [1, 0], 3: [2,0], 4:[0, 1], 5:[1, 1], 6:[2,1], 7:[0,2], 8:[1,2], 9:[2,2], 0:[1, 3]}
# x = 1
# y = [1, 3, 5]
# if x in [1,3,5]:
#     print(x)