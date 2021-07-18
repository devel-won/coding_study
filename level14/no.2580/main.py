import sys

Map = []
zero_list = []
for i in range(9):
    col = list(map(int, sys.stdin.readline().strip().split()))
    Map.append(col)

    for index, j in enumerate(col):
        if j == 0:
            zero_list.append([i, index])


def check(x, y):
    A = [i for i in range(1, 10)]
    for i in range(9):
        if Map[x][i] in A:
            A.remove(Map[x][i])
        if Map[i][y] in A:
            A.remove(Map[i][y])

    for i in range(x//3 * 3, (x // 3 + 1) * 3):
        for j in range(y//3 * 3, (y // 3 + 1) * 3):
            if Map[i][j] in A:
                A.remove(Map[i][j])
    return A


def dfs():
    global Map
    if len(zero_list) == 0:
        return 1

    i, j = zero_list[-1]


    for s in check(i, j):
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

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0