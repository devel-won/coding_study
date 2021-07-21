import sys

Map = []
zero_list = []
n = 0
row = [[False]*9 for _ in range(9)]
col = [[False]*9 for _ in range(9)]
squ = [[False]*9 for _ in range(9)]

for i in range(9):
    col2 = list(map(int, sys.stdin.readline().strip().split()))
    Map.extend(col2)

    for index, j in enumerate(col2):
        if j == 0:
            zero_list.append([i, index])
            n += 1
        else:
            row[i][j-1] = True
            col[index][j-1] = True
            squ[i//3*3+index//3][j-1] = True


def dfs(x):
    global Map
    if x == n:
        for s in range(9):
            print(' '.join(map(str, Map[s * 9:(s + 1) * 9])))
        exit(0)

    a, b = zero_list[x]

    for k2 in range(1, 10):
        k = k2 - 1
        if not(row[a][k] or col[b][k] or squ[a//3*3+b//3][k]):
            row[a][k] = col[b][k] = squ[a // 3 * 3 + b // 3][k] = True
            Map[a*9 + b] = k2
            dfs(x + 1)
            row[a][k] = col[b][k] = squ[a // 3 * 3 + b // 3][k] = False
            Map[a * 9 + b] = 0


dfs(0)
