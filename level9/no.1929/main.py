M, N = map(int, input().split())
result = []


def d(x):
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return i
    return x


for i in range(M, N+1):
    if i == 1:
        pass
    else:
        if d(i) == i:
            print(i)
