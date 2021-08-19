def checkBracket(s):
    checkB = True
    stackBracket = []

    for i in range(len(s)):
        if not stackBracket and (s[i] == ')' or s[i] == ']' or s[i] == '}'):
            checkB = False
            return checkB

        if s[i] in ('[', '(', '{'):
            stackBracket.append(s[i])
        else:
            x= stackBracket.pop()
            if s[i] == ')' and x != '(':
                checkB = False
                return checkB
            elif s[i] == ']' and x != '[':
                checkB = False
                return checkB
            elif s[i] == '}' and x != '{':
                checkB = False
                return checkB
    return checkB

def solution(s):
    if len(s) % 2 != 0:
        return 0

    answer = 0
    for i in range(len(s)-1):
        new_s = s[i:] + s[:i]

        if checkBracket(new_s):
            answer += 1

    return answer

solution("[](){}")
solution("}]()[{")
solution("[)(]")
