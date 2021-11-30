import sys

A = int(sys.stdin.readline(), 2)
B = int(sys.stdin.readline(), 2)
temp = 2**100000 -1
print(bin(A&B)[2:].zfill(100000))
print(bin(A|B)[2:].zfill(100000))
print(bin(A^B)[2:].zfill(100000))
print(bin(A^temp)[2:].zfill(100000))
print(bin(B^temp)[2:].zfill(100000))
