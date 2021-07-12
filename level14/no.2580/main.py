import sys

Map = []
for i in range(9):
    Map.append(list(map(int, sys.stdin.readline().strip().split())))


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
    count = 1
    for i in range(9):
        for j in range(9):
            if Map[i][j] == 0:
                count = 0
                for s in range(1, 10):
                    if check(i, j, s):
                        Map[i][j] = s
                        if dfs():
                            return 1
                        else:
                            Map[i][j] = 0
    if count:
        return 1
    else:
        return 0

dfs()

for i in Map:
    for j in i:
        print(j, end=' ')
    print()
