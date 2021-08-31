from itertools import permutations


def calculate(op, exp):
    temp = ''
    temp_array = []
    for i in exp:
        if i.isdigit() == True:
            temp += i
        else:
            temp_array.append(temp)
            temp_array.append(i)
            temp = ''
    temp_array.append(temp)

    for o in op:
        stack = []
        while len(temp_array) != 0:
            print(':::::', stack)
            t = temp_array.pop(0)
            if t == o:
                x = ''
                if o == '+':
                    x = str(int(stack.pop()) + int(temp_array.pop(0)))
                elif o == '-':
                    x = str(int(stack.pop()) - int(temp_array.pop(0)))
                elif o == '*':
                    x = str(int(stack.pop()) * int(temp_array.pop(0)))
                stack.append(x)
            else:
                stack.append(t)
            print(stack)
        temp_array = stack

    return abs(int(stack[0]))

def solution(expression):

    operations = ['-', '+', '*']
    operations = list(permutations(operations, 3))
    result = []

    for op in operations:
        result.append(calculate(op, expression))

    return max(result)

solution("100-200*300-500+20") #60420
# solution("50*6-3*2"	) #300