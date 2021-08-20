def solution(p):
    if not p:
        return ""
    u,v = seperate(p)

    if isBalanced(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

def seperate(p):
    left_count = 0
    right_count = 0
    for idx, i in enumerate(p):
        if i == '(':
            left_count += 1
        elif i == ')':
            right_count += 1
        if left_count == right_count:
            return p[:idx + 1], p[idx + 1:]


def isBalanced(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True