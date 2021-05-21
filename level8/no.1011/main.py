T = int(input())

for _ in range(T):

    A, B = map(int, input().split())
    X = B - A
    count = 0
    max_value = 1

    while(True):
        if X == 1:
            count += 1
            break
        else:
            X -= 2 * max_value
            count += 2
            max_value += 1
            if X <= max_value:
                count += 1
                break
            elif X <= 2 * max_value:
                count += 2
                break

    print(count)
