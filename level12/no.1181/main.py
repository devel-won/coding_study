import sys

T = int(sys.stdin.readline().strip())

A = []

for _ in range(T):
    char = sys.stdin.readline().strip()
    A.append(char)

B = list(map(lambda x: [x, len(x)], set(A)))

B.sort(key=lambda x: (x[1], x[0]))

for i in B:
    print(i[0])
