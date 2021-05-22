N = int(input())
input_list = list(map(int, input().split()))


def d(x):
    if x == 1:
        return 0
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return 0
    return 1


print(sum(map(d, input_list)))
