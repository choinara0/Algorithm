def solution(s):
    answer = True
    s_length = int(len(s))
    if s_length == 4 or s_length ==6:
        for i in range(s_length):
            if not s[i].isdigit():
                return False
        return True
    else:
        return False


a = "1234"
print(a[1].isdigit())