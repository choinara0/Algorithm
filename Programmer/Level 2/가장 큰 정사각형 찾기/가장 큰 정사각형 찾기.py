def solution(board):
    answer = 0
    n = len(board) #세로
    m = len(board[0]) #가로

    dp = [[0]*m for i in range(n)]
    dp[0] = board[0]
    for i in range(1, n):
        dp[i][0] = board[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    for i in range(n):
        temp = max(dp[i])
        answer = max(answer ,temp)
    answer = answer ** 2

    return answer

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])

'''
board 
0 1 1 1
1 1 1 1
1 1 1 1
0 0 1 0

dp
0 1 1 1 
1 1 2 2 
1 2 2 3 
0 0 2 0
'''