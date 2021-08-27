
def solution(msg):
    answer = []
    LZW_dict = dict()

    for i in range(65, 91):
        LZW_dict[chr(i)] = i-64
    start = 0
    end = len(msg)
    while start<=len(msg):
        temp = msg[start:end]

        if temp in LZW_dict.keys():
            answer.append(LZW_dict[temp])
            if end >= len(msg):
                break
            LZW_dict[temp+msg[end]] = max(LZW_dict.values()) + 1

            start = end
            end = len(msg)
        else:
            end-=1

    return answer

solution('KAKAO') #[11, 1, 27, 15]
solution('TOBEORNOTTOBEORTOBEORNOT') # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
solution('ABABABABABABABAB') #[1, 2, 27, 29, 28, 31, 30]