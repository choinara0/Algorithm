def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    new_String = s.upper()
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in new_String:
        if i=='P':
            p_count += 1
        elif i =='Y':
            y_count +=1
    if p_count == y_count:
        return True
    else:
        return False

solution('hi')