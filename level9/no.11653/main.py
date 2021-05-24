N = int(input())
result = []


def d(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return i
    return x


if N == 1:
    pass
else:
    while True:
        y = d(N)
        result.append(y)
        if y == N:
            break
        else:
            N //= y

    for j in result:
        print(j)
