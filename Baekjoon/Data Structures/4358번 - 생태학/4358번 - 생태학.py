import sys
from collections import defaultdict

trees = defaultdict(int)
n = 0
while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break
    trees[tree] += 1
    n += 1

trees_list = sorted(list(trees.keys()))
for tree in trees_list:
    print('%s %.4f' %(tree, trees[tree]/n*100))