def solution(genres, plays):
    answer = []
    hash1 = {}
    hash2 = {}

    for i in range(len(genres)):
        if genres[i] in hash1:
            hash1[genres[i]] += plays[i]
        else:
            hash1[genres[i]] = plays[i]

        if genres[i] not in hash2:
            hash2[genres[i]] = [(plays[i], i)]
        else:
            hash2[genres[i]].append((plays[i], i))

    for k, v in sorted(hash1.items(), key=lambda x:x[1], reverse=True):
        for n, i in sorted(hash2[k], key=lambda x:x[0], reverse=True)[:2]:
            answer.append(i)

    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) #[4, 1, 3, 0]
