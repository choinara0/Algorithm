def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    for i in range(len(arr1)):
        temp=bin(arr1[i])[2:]
        while(len(temp)!=n):
            temp = '0'+temp
        arr1_bin.append(temp)
    arr2_bin = []
    for i in range(len(arr2)):
        temp = bin(arr2[i])[2:]
        while(len(temp)!=n):
            temp = '0' + temp
        arr2_bin.append(temp)
    for i in range(len(arr1_bin)):
        temp1 = arr1_bin[i]
        temp2 = arr2_bin[i]
        answer_temp = ''
        for j in range(len(temp1)):
            if temp1[j] == '1' or temp2[j] == '1':
                answer_temp+='#'
            else:
                answer_temp+=' '
        answer.append(answer_temp)
    print(answer)
    print(arr1_bin, arr2_bin)

    return answer
solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])


temp=bin(3)[2:]
while(len(temp)!=5):
    temp = '0'+temp
print(temp)