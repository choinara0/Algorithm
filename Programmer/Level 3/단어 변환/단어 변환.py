def dfs(begin, target, words, visited):
    stacks = [begin]

    while stacks:
        s = stacks.pop()
        if s == target:
            return answer
        for w in range(len(words)):
            if len([i for i in range(len(words[w])) if words[w][i] != stacks[i]]) ==1 :
                if visited[w] != 0:
                    continue
                visited[w] = 1
                stacks.append(words[w])
        answer += 1



def solution(begin, target, words):
    global answer
    answer = 0

    if target not in words:
        return 0

    visited = [0 for i in range(len(words))]
    dfs(begin, target, words, visited)


    return answer

solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]	)
solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"])