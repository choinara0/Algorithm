'''
2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다.
드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다.

도연이가 다니는 대학의 캠퍼스는  크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다.
예를 들어, 도연이가 (x,y)에 있다면 이동할 수 있는 곳은 (x,y+1 ), (x,y-1 ), (x+1,y), (x-1,y )이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.

불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.

입력
첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수  N(1<=N<=600),  M(1<=M<=600)이 주어진다.
둘째 줄부터 개의 줄에는 캠퍼스의 정보들이 주어진다. O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.

출력
첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력한다.

입력 예)   출력예)
3 5         1
OOOPO
OIOOX
OOOXP

'''
'''
출처 :  University > 숙명여자대학교 > 제1회 숙명여자대학교 교내 알고리즘 경진대회 (SMUPC) C번
문제를 검수한 사람: cs71107, lky7674, plast, sait2000, songfox00, wbcho0504, whaeun25
문제를 만든 사람: swoon
'''
def dfs(r, c):
    visited[r][c] = 1
    if matrix[r][c] == 'P':
        global meet
        meet += 1
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m and visited[nx][ny]==0:
            if matrix[nx][ny] != 'X':
                dfs(nx, ny)
    return

n, m = map(int, input().split())
visited = [[0]*m for i in range(n)]
matrix = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
meet = 0
for i in range(n):
    row = list(input())
    for j in range(len(row)):
        if "I" == row[j]:
            start_node_r = i
            start_node_c = j
    matrix.append(row)
dfs(start_node_r, start_node_c)

if meet==0:
    print("TT")
else:
    print(meet)





