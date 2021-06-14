
def solution(n):
    convert_n_to_3 = ''
    while (1):
        convert_n_to_3 = str(n % 3) + convert_n_to_3
        n //= 3
        if n == 0:
            break

    reverse_convert_n_to_3 = convert_n_to_3[::-1]
    convert_n_to_10 = 0
    for i in range(len(reverse_convert_n_to_3)):
        convert_n_to_10 += int(reverse_convert_n_to_3[i]) * (3 ** (len(reverse_convert_n_to_3) - 1 - i))
    print(convert_n_to_10)

    return convert_n_to_10