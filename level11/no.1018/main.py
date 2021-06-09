M, N = map(int, input().split())

all_list = []

max_value = 64

white_sample = [["B" if (a + b) % 2 == 1 else "W" for b in range(8)] for a in range(8)]
black_sample = [["W" if (c + d) % 2 == 1 else "B" for d in range(8)] for c in range(8)]

for _ in range(M):
    all_list.append(list(input()))

for i in range(M-7):
    for j in range(N-7):
        white_count = 0
        black_count = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if all_list[x][y] != white_sample[x-i][y-j]:
                    white_count += 1
                if all_list[x][y] != black_sample[x-i][y-j]:
                    black_count += 1
        if max_value > white_count:
            max_value = white_count
        if max_value > black_count:
            max_value = black_count

print(max_value)
