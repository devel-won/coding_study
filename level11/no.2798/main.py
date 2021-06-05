N, M = map(int, input().split())

C = list(map(int, input().split()))

result = 0

for x in C:
    for y in C:
        if y == x:
            pass
        else:
            for z in C:
                if z == y or z == x:
                    pass
                else:
                    s = x + y + z
                    if result < s <= M:
                        result = s

print(result)
