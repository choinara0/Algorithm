def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(w, h):
    answer = 0
    if w == h:
        answer =  (w * h - w)
        return answer
    elif w > h:
        big = w
        small = h
    else:
        big = h
        small = w

    g = gcd(big, small)
    answer = w * h - (w + h -g)

    return answer

solution(8, 12) # 80
