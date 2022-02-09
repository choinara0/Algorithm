import sys

N, M = map(int, sys.stdin.readline().split())
dna_list = []
for _ in range(N):
    dna_list.append(input())

answer = ''
hamming_distance = 0

for i in range(M):
    count = [0, 0, 0, 0]
    for j in range(N):
        if dna_list[j][i] == 'A':
            count[0] += 1
        elif dna_list[j][i] == 'C':
            count[1] += 1
        elif dna_list[j][i] == 'T':
            count[2] += 1
        elif dna_list[j][i] == 'G':
            count[3] += 1

    idx_max_dna = count.index(max(count))
    if idx_max_dna == 0:
        answer += 'A'
    elif idx_max_dna == 1:
        answer += 'C'
    elif idx_max_dna == 2:
        answer += 'T'
    elif idx_max_dna == 3:
        answer += 'G'
    hamming_distance += N - max(count)

print(answer)
print(hamming_distance)
