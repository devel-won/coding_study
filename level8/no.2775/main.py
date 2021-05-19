import sys

T = int(sys.stdin.readline())


def d(a, b, f):
    floor = []
    s = 0
    if b == 1:
        return 1
    elif a == 0:
        return f[b-1]

    for i in range(b):
        s += f[i]
        floor.append(s)
    return d(a - 1, b, floor)


for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    floor = [i + 1 for i in range(n)]

    print(d(k, n, floor))
