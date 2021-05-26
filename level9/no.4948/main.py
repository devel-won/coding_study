def d(x, y):
    for j in y:
        if x % j == 0:
            return j
    return x


all_list = [1 for i in range(123456 * 2 + 1)]
all_list[0] = 0

for i in range(2, int(123456 * 2 ** 0.5) +1):
    if all_list[i] == 1:
        num = 2
        while i * num <= 123456 * 2:
            all_list[i * num] = 0
            num += 1

while True:
    N = int(input())
    if N == 0:
        break
    elif N == 1:
        print(1)
    else:
        print(sum(all_list[N+1:2*N]))
