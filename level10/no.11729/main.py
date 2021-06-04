def d(x, y, z, n):
    if n <= 0:
        return
    d(x, z, y, n-1)
    print(x, z)
    d(y, x, z, n-1)


def t(n):
    if n == 0:
        return 0
    return 2*t(n-1) + 1


N = int(input())

print(t(N))
d(1, 2, 3, N)
