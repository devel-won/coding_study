N = int(input())

result = 0

for _ in range(N):
    A = input()
    count = 0
    char = None
    set_A = len(set(A))

    for i in A:
        if i != char:
            char = i
            count += 1

    if count == set_A:
        result += 1

print(result)
