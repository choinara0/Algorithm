def solution(n, words):
    answer = []
    count = 1
    for i in range(1, len(words)):
        count = count % n
        if (words[i][0] != words[i-1][-1]) or words[i] in words[:i]:
            answer = [count + 1, 1 + i//n]
            print(answer)
            return answer
        count += 1
    if not answer:
        answer = [0, 0]
        print(answer)
        return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]	)