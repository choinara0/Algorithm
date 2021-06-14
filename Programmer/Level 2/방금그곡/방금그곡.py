from datetime import datetime

def replace_melody(s):
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    s = s.replace('A#', 'a')
    return s

def solution(m, musicinfos):
    answer = []
    m = replace_melody(m)

    for i in range(len(musicinfos)):
        start, end, title, melody = musicinfos[i].split(',')
        start = datetime.strptime(start, '%H:%M')
        end = datetime.strptime(end, '%H:%M')
        play_time = (end - start).seconds // 60
        melody = replace_melody(melody)

        if len(melody) >= play_time:
            melody = melody[:play_time]
        else:
            a = int(play_time / len(melody))
            b = play_time % len(melody)
            melody = melody * a + melody[:b]

        if m in melody:
            answer.append([title, play_time, i])

    if len(answer) != 0:
        answer = sorted(answer, key=lambda x:(-x[1], x[2]))
        return answer[0][0]
    else:
        return '(None)'

# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B", "03:00,03:30,HE,CC#B"])

