def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp_arr = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            temp_arr.append(temp)
            print(temp_arr)
        answer.append(temp_arr)
    print(answer)
    return answer

solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) #[[15, 15], [15, 15], [15, 15]]
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) #[[22, 22, 11], [36, 28, 18], [29, 20, 14]]