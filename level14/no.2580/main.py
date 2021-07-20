import sys

Map = []
zero_list = []
row = [[False]*9 for _ in range(9)]
col = [[False]*9 for _ in range(9)]
squ = [[False]*9 for _ in range(9)]

for i in range(9):
    col = list(map(int, sys.stdin.readline().strip().split()))
    Map.extend(col)

    for index, j in enumerate(col):
        if j == 0:
            zero_list.append([i, index])
        else:
            row[i][j] = True
            col[index][j] = True


def check(x, y):
    A = [i for i in range(1, 10)]
    for i in range(9):
        if Map[x*9 + i] in A:
            A.remove(Map[x*9 + i])
        if Map[i*9 + y] in A:
            A.remove(Map[i*9 + y])

    x1 = x//3
    y1 = y//3

    for i in range(x1 * 3, (x1 + 1) * 3):
        for j in range(y1 * 3, (y1 + 1) * 3):
            if Map[i * 9 + j] in A:
                A.remove(Map[i * 9 + j])
    return A


def dfs():
    global Map
    if len(zero_list) == 0:
        return 1

    i, j = zero_list[-1]

    for s in check(i, j):
        Map[i * 9 + j] = s
        del zero_list[-1]
        if dfs():
            return 1
        else:
            zero_list.append([i, j])
            Map[i * 9 + j] = 0
    return 0


dfs()

for i in range(9):
    print(' '.join(map(str, Map[i * 9:(i + 1) * 9])))

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0