'''
DFS(깊이 우선 탐색)는 Stack, BFS(넓이 우선 탐색)는 Queue.

'''

#예제 1
def DFS(start_node):
    # 1) stack 에 첫 번째 노드 넣으면서 시작
    stack = [start_node, ]

    while True:
        # 2) stack이 비어있는지 확인
        if len(stack) == 0:
            print('All node searched.')
        return None

        # 3) stack에서 맨 위의 노드를 pop
        node = stack.pop()

        # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print('The target found.')
        return node

        # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)

        # 6) children을 stack에 쌓기
        stack.extend(children)

        # 7) 이렇게 target을 찾거나, 전부 탐색해서 stack이 빌 때까지 while문 반복


#예제 2
def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))