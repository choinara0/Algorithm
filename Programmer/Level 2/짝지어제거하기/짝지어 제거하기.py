def solution(s):
    answer = 0
    stack = []
    for i in s:
        if len(stack)>=1:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(stack)
    if stack:
        return 0
    else:
        return 1
    return answer

solution('baabaa')