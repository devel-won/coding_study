import sys

T = int(sys.stdin.readline())

b = [0 for i in range(10001)]

for _ in range(T):
    b[int(sys.stdin.readline())] += 1

for y, z in enumerate(b):
    for _ in range(z):
        print(y)
