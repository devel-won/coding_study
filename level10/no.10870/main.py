N = int(input())


def d(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return d(x-2) + d(x-1)


print(d(N))
