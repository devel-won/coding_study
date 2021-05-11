N = int(input())

for _ in range(N):
    point = 0
    result = 0
    for i in input():
        if i == 'O':
            point += 1
            result += point
        else:
            point = 0
    print(result)
