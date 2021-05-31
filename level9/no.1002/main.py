T = int(input())

for _ in range(T):

    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    X = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5

    od = r1 + r2
    id = abs(r1-r2)

    if ((X == 0) and (r1 != r2)) or ((X != 0) and ((od < X) or (id > X))):
        print(0)
    elif (X == 0) and (r1 == r2):
        print(-1)
    elif X != 0 and (X == od or X == id):
        print(1)
    else:
        print(2)
