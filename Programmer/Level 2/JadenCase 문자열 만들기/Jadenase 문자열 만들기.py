
def solution(s):
    answer = ''
    s_split = s.split(' ')
    for i in range(len(s_split)):
        s_split[i] = s_split[i].capitalize()
    answer = ' '.join(s_split)
    return answer

solution("3people unFollowed       me")