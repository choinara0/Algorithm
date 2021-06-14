def solution(s):
    len_new_s = [len(s)]
    for i in range(1, len(s)):
        new_s = ""
        splited = [s[j:j+i] for j in range(0, len(s), i)]
        stack = [[splited[0], 1]]


        for k in splited[1:]:
            if stack[-1][0] != k:
                stack.append([k, 1])
            else:
                stack[-1][1] += 1
        new_s += ''.join([str(cnt) + word if cnt > 1 else word for word, cnt in stack])
        len_new_s.append(len(new_s))
    print(len_new_s)
    return min(len_new_s)

solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")