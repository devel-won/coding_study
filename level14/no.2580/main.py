import sys

Map = []
zero_list = []
for i in range(9):
    col = list(map(int, sys.stdin.readline().strip().split()))
    Map.extend(col)

    for index, j in enumerate(col):
        if j == 0:
            zero_list.append([i, index])


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

# for i in Map:
#     for index, j in enumerate(i):
#         if index == 8:
#             print(j)
#         else:
#             print(j, end=' ')

for i in range(9):
    print(' '.join(map(str, Map[i * 9:(i + 1) * 9])))

# for i in Map:
#     print(' '.join(map(str, i)))

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0