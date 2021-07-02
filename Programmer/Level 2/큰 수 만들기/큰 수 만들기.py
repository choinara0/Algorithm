def solution(number, k):
    answer = ''

    stack = []
    for i in number:
        while stack and int(i)>int(stack[-1]):
            if k>0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)


    if k>0:
        for i in range(k):
            stack.pop()

    answer = "".join(stack)


    return answer

solution("4177252841", 4)

