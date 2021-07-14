import sys

Map = []
zero_list = []
for i in range(9):
    col = list(map(int, sys.stdin.readline().strip().split()))
    Map.append(col)

    for index, j in enumerate(col):
        if j == 0:
            zero_list.append([i, index])


def check(x, y, num):
    for i in range(9):
        if Map[x][i] == num or Map[i][y] == num:
            return 0

    for i in range(x//3 * 3, (x // 3 + 1) * 3):
        for j in range(y//3 * 3, (y // 3 + 1) * 3):
            if Map[i][j] == num:
                return 0
    return 1


def dfs():
    global Map
    if len(zero_list) == 0:
        return 1

    i, j = zero_list[-1]

    for s in range(1, 10):
        if check(i, j, s):
            Map[i][j] = s
            del zero_list[-1]
            if dfs():
                return 1
            else:
                zero_list.append([i, j])
                Map[i][j] = 0

    return 0

dfs()

for i in Map:
    for index, j in enumerate(i):
        if index == 8:
            print(j)
        else:
            print(j, end=' ')
