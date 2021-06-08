T = int(input())

list_all = []

for _ in range(T):
    W, H = map(int, input().split())
    list_all.append([W, H])

for w, h in list_all:
    count = 0
    for w2, h2 in list_all:
        if w < w2 and h < h2:
            count += 1
    print(count+1, end=' ')
