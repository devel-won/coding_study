def function(a):
    list_a = list(map(int, list(str(a))))
    x = 0
    for i in range(len(list_a)-1):
        if i == 0:
            x = list_a[i] - list_a[i + 1]
        else:
            if list_a[i] - list_a[i+1] != x:
                return 0
    return 1

print(sum([function(i + 1) for i in range(int(input()))]))
