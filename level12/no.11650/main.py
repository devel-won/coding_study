import sys

T = int(sys.stdin.readline())

A = []

for _ in range(T):
    A.append(list(map(int, sys.stdin.readline().split())))

A.sort()

for i in A:
    print(i[0], i[1])
