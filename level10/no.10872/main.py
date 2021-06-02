N = int(input())


def d(x):
    if x == 0:
        return 1
    else:
        return d(x-1) * x


print(d(N))
