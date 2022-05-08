def solution(phone_book):
    answer = True
    hash = {}

    for phone_num in phone_book:
        hash[phone_num] = 1

    for phone_num in phone_book:
        temp = ''
        for num in phone_num:
            temp += num
            if temp in hash and temp != phone_num:
                answer = False
                break

    return answer

solution(["119", "97674223", "1195524421"]) #False
solution(["123","456","789"]) #True
solution(["12","123","1235","567","88"]) #False