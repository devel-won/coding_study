while True:
    A = list(map(int, input().split()))

    if min(A) == 0:
        break

    max_value = max(A)
    A.remove(max_value)
    result = 0

    for i in A:
        result += i ** 2

    if max_value ** 2 == result:
        print("right")
    else:
        print("wrong")
