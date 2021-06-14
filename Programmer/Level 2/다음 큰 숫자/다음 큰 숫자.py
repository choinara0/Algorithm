def solution(n):
    answer = 0
    bin_n = str(bin(n))[2:]
    sum_bin_n = 0
    for i in range(len(bin_n)):
        if bin_n[i] == '1':
            sum_bin_n += 1

    print(bin_n)
    while(1):
        n = n+1
        bin_new_n = str(bin(n))[2:]
        sum_bin_new_n = 0
        print(bin_new_n)
        for i in range(len(bin_new_n)):
            if bin_new_n[i] == '1':
                sum_bin_new_n += 1
        if sum_bin_new_n == sum_bin_n:
            answer = n
            break
    print(answer)
    return answer

solution(15)