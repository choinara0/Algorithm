import sys

S = sys.stdin.readline().strip()
s_len = len(S)

for i in range(s_len):
    if S[i:] == S[i:][::-1]:
        print(s_len + i)
        break