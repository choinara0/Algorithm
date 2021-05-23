'''

'''

def solution(board, moves):
    answer = 0
    stack = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1]>=1:
                stack.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                while(len(stack)>=2):
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                    else:
                        break
                break

    print(answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])


'''

'''



