import sys
input = sys.stdin.readline
K, L = map(int, input().split())
hash = {}

for i in range(L):
    student_id = input().strip()

    if student_id in hash:
        del hash[student_id]
        hash[student_id] = 1
    else:
        hash[student_id] = 1

print('\n'.join(map(str, list(hash)[0:K])))