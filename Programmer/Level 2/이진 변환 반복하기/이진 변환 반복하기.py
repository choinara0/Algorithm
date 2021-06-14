
def remove_zero(s):
    new_s = s.replace('0', '')
    del_zero_cnt = len(s) - len(new_s)
    return del_zero_cnt, new_s

def solution(s):
    answer = []
    cnt_to_bin = 0
    total_remove_cnt = 0
    while(1):
        new_cnt, s = remove_zero(s)
        cnt_to_bin += 1
        total_remove_cnt += new_cnt

        if len(s) == 1:
            break
        else:
            s = bin(len(s))[2:]

    answer.append(cnt_to_bin)
    answer.append(total_remove_cnt)

    return answer

solution("110010101001")
solution("01110")
solution("1111111")

