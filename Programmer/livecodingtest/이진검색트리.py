'''
이진검색트리란 각 노드마다 왼쪽 서브트리에는 해당 노드의 값보다 작은 값들이 존재하며, 노드의 왼쪽 서브트리에는 그 노드의 값보다 같거나 큰 값들이 존재하는 정렬된 트리를 말합니다.
이진 검색 트리가 주어졌을때, 그 트리에서 k번째 작은 노드의 값을 구하시오.

입출력 예
입력: 입력으로는 트리를 '직렬화'하여 표현한 배열(문자열)과 목표 크기인 'k'가 주어집니다.

왼쪽 트리 직렬화 : "3,1,4,null,2,null,null" (아래 그림 왼쪽 트리의 예)
오른쪽 트리 직렬화 : "5,3,6,2,4,null,null,1,null,null,null,null,null,null,null" (아래 그림 오른쪽 트리의 예)
출력: 'k'번째 크기에 해당하는 트리 상의 값을 출력합니다.

'''



def solution(data, k):

    temp = [data[i] for i in range(len(data)) if data[i]!=',' and data[i].isdigit()]
    temp.sort()


    return int(temp[k-1])

solution("3,1,4,null,2,null,null", 1)
solution("5,3,6,2,4,null,null,1,null,null,null,null,null,null,null", 3)