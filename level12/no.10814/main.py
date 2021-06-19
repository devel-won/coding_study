import sys

T = int(sys.stdin.readline().strip())

A = []

count = 0

for _ in range(T):
    age, name = sys.stdin.readline().strip().split()
    A.append([int(age), name, count])
    count += 1

A.sort(key=lambda x: (x[0], x[2]))

for i in A:
    print(i[0], i[1])
