def solution(files):
    answer = []
    temp = []
    for file in files:
        head, number, tail = '', '', ''
        num_check = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                num_check = True
            elif num_check is False:
                head += file[i]
            else:
                tail = file[i:]
                break

        temp.append((head, number, tail))
    temp.sort(key=lambda x: (x[0].upper(), int(x[1])))
    for i in temp:
        answer.append(''.join(i))

    return answer

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])