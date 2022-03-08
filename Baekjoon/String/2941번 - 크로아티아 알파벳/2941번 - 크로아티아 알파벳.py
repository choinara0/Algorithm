import sys

word = sys.stdin.readline().strip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = len(word)
for c in croatia:
    answer -= word.count(c)
print(answer)