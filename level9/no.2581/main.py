A = int(input())
B = int(input())

result = 0
min_value = 0
for i in range(A, B+1):
    check = 0
    if i == 1:
        pass
    else:
        for j in range(2, i):
            if i % j == 0:
                check = 1
                break
        if check == 0:
            if min_value == 0:
                min_value = i
            result += i

if result == 0:
    print(-1)
else:
    print(result)
    print(min_value)
