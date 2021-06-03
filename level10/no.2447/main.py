def d(x, y, n):
    if n == 1:
        A[x][y] = '*'
        return
    a = n // 3

    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                d(x+a*i, y+a*j, a)


N = int(input())
A = [[' ']*N for _ in range(N)]

d(0, 0, N)

for i in A:
    for j in i:
        print(j, end='')
    print('')
