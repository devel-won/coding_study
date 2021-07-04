import sys

Map = []
for i in range(9):
    Map.append(list(map(int, sys.stdin.readline().strip().split())))


def check(x, y, num):
    for i in range(9):
        if Map[x][i] == num or Map[i][y] == num:
            return 0

    for i in range(x//3 * 3, (x // 3 + 1) * 3):
        for j in range((y//3 * 3, (y // 3 + 1) * 3)):
            if Map[i][j] == num:
                return 0
    return 1


def dfs(x, y):
    for i in range(9):
        for j in range(9):
            if Map[i][j] == 0:


                pass

print("check")
