N = input()

num_size = len(N)

result = 0

for i in range(num_size * 9, num_size - 2, -1):
    x = int(N) - i

    if x > 0:
        tmp = list(map(int, list(str(x))))
        tmp.append(x)
        if sum(tmp) == int(N):
            result = x
            break

print(result)
