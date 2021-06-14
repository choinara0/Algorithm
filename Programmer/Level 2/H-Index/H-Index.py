def solution(citations):

    citations.sort()
    max_arr = citations[-1]
    min_arr = citations[0]
    max_h = 0

    for i in range(min_arr, max_arr+1):
        cnt = 0

        for j in range(len(citations)):
            if citations[j] >= i:
                cnt += 1

        if cnt>=i and len(citations)-cnt <= i and max_h < i:
            max_h = i

        print(max_h)
    if min_arr >= len(citations):
        max_h = len(citations)
    return max_h

solution([3,0,6,1,5])
solution([9,8,7])
# solution([1, 2, 3, 4]) -> return 2



