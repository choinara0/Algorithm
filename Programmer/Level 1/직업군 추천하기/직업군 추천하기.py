def solution(table, languages, preference):
    answer = ''
    score_table = dict()
    for i in range(len(table)):
        temp_table = table[i].split()
        sum = 0
        for j in range(len(languages)):
            if languages[j] in temp_table:
                sum += preference[j] * (6- temp_table.index(languages[j]))

        score_table[table[i].split()[0]] = sum

    m1 = 0
    for k, v in score_table.items():
        if v > m1:
            answer = k
            m1 = v
        elif v == m1:
            if k < answer:
                answer = k

    return answer


solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5])
solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],	["JAVA", "JAVASCRIPT"],	[7, 5])