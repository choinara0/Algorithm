def solution(s):
    answer = ''
    s_len = int(len(s))
    if s_len%2!=0:
        temp = int(s_len/2)
        answer += s[temp]
    else:
        temp1 = int(s_len/2 -1)
        temp2 = int(s_len/2)
        answer += s[temp1]
        answer += s[temp2]
    print(answer)
    return answer

solution('abcd')