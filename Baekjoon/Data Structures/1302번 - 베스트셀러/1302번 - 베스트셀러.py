import sys

N = int(sys.stdin.readline())
books = {}

for _ in range(N):
    book = sys.stdin.readline().strip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

best_value = max(books.values())
best_books = []

for key, value in books.items():
    if value == best_value:
        best_books.append(key)

print(sorted(best_books)[0])