def d(x, y):
    for j in y:
        if x % j == 0:
            return j
    return x


all_list = [1 for i in range(10000)]
all_list[0:1] = [0, 0]
num_list = []


for i in range(2, int(10000 ** 0.5) +1):
    if all_list[i] == 1:
        num = 2
        while i * num <= 10000:
            all_list[i * num] = 0
            num += 1

num = 0
for i in all_list:
    if i == 1:
        num_list.append(num)
    num += 1

T = int(input())

for _ in range(T):
    N = int(input())
    tmp_list = list(filter(lambda x: x <= N/2, num_list))
    tmp_list.reverse()

    for i in tmp_list:
        if (N - i) in num_list:
            print(i, N-i)
            break
